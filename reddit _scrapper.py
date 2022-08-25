import praw
import matplotlib.pyplot as plt
import pandas as pd
#top secret data 
reddit = praw.Reddit(client_id='SeLIOb6jTNWpTpfxnFksmw', \
                     client_secret='_y40zXg1jWnm8zaHdUReMGm4oPxgoA', \
                     user_agent='Comment Scrapper for Reddit', \
                     username='froggy-b', \
                     password='Gi0Gi01234!')

subredditname = "OnePiece"

subreddit = reddit.subreddit(subredditname)

top_subbreddit = subreddit.top()
count = 0
max = 100000
print('success')
words = []
wordCount = {}
commonWords = {'that','this','and','of','the','for','I','it','has','in',
'you','to','was','but','have','they','a','is','','be','on','are','an','or',
'at','as','do','if','your','not','can','my','their','them','they','with',
'at','about','would','like','there','You','from','get','just','more','so',
'me','more','out','up','some','will','how','one','what',"don't",'should',
'could','did','no','know','were','did',"it's",'This','he','The','we',
'all','when','had','see','his','him','who','by','her','she','our','thing','-',
'now','what','going','been','we',"I'm",'than','any','because','We','even',
'said','only','want','other','into','He','what','i','That','thought',
'think',"that's",'Is','much'}
print('getting the forests')
for submission in subreddit.top(time_filter = "month", limit=1000):
    submission.comments.replace_more(limit=10)
    for top_level_comment in submission.comments:
        count += 1
        if(count == max):
            break
        word = ""
        for letter in top_level_comment.body:
            if(letter == ' '):
                if(word and not word[-1].isalnum()):
                    word = word[:-1]
                if not word in commonWords:
                    words.append(word)
                word = ""
            else:
                word += letter
    if(count == max):
            break

for word in words:
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1

sortedList = sorted(wordCount, key = wordCount.get, reverse = True)

keyWords = []
keyCount = []
amount = 0

df = pd.DataFrame(sortedList)
#dp = pd.DataFrame(keyCount)
print('saving')
df.to_csv('reddit_comments.csv' , index = False)
print('done')
#dp.to_csv('reddit_comments_count.csv' , index = False)

#for entry in sortedList:
#    keyWords.append(entry)
#    keyCount.append(wordCount[entry])
#    amount += 1
#    if (amount == 10):
#        break

#labels = keyWords
#sizes = keyCount
# explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

#plt.title('Top comments for: r/' + subredditname)
#plt.pie(sizes, labels=labels, autopct='%1.1f%%',
#        shadow=True, startangle=90)
#plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

#plt.show()

