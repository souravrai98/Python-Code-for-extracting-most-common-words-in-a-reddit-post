import praw
from nltk.corpus import stopwords
import re
from itertools import chain
from collections import Counter


#Create a reddit app to get all the below deatils on https://www.reddit.com/prefs/apps 
reddit = praw.Reddit(
    client_id="",
    client_secret="",
    password="",
    user_agent="",
    username="",
)

submission = reddit.submission(url="https://www.reddit.com/r/anime/comments/m6odg8/your_top_10_anime_list/") 
submissionList = []
submission.comments.replace_more(limit=None)
for comment in submission.comments.list():         # Getting the list of all the comment ID's in the reddit post
    submissionList.append(comment)


def word_extraction(sentence):    # Function for removing all the stop words
  ignore = stopwords.words('english')  
  words = re.sub("[^\w]", " ",  sentence).split()    
  cleaned_text = [w.lower() for w in words if w not in ignore]    
  return cleaned_text


def data_cleaning(comments):   # Function to clean the data 
    lower_l = [comment.body.lower() for comment in comments]
    
    sans_virgules = [address.replace(',', ' ') for address in lower_l]
    sans_virgules_1 = [address.replace('\n', ' ') for address in sans_virgules]


    nostopwords = []
    for l in sans_virgules_1:
        nostopwords.append(word_extraction(l))
        
    return nostopwords

cleaned = data_cleaning(submissionList)

print(Counter(chain(*cleaned)).most_common(80))      
