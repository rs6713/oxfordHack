from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask_assets import Environment, Bundle
import tweepy

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

@app.route('/')
def main_page():
    #fetch twitter data


    auth = tweepy.OAuthHandler("4demSjUhdVopc5p2IH1rlZPI9", "c3zPuNUjOvfreAxIdwgPTbsx3OJnvNY595VC0lmbs09PcNUtgm")
    auth.set_access_token("391666744-uoByvtlyK64IYKQGiNJO7St7rl1TnGUfRDggdYua", "D0VqdC8iXW0N6YEJLPk6YYYsmiSe29p7hgSvFiBaGEAXI")

    api = tweepy.API(auth)

    #how to you compare to friends api.friends
    user= "hacksmiths"#"BecksTSimpson"
    public_tweets = api.user_timeline(id=user,count=50)
    
    #print str(public_tweets[0])
    
    for i, tweet in enumerate(public_tweets):
        tw=str(tweet.text)
        #print (tw[0:2])
        if(tw[0:2]== "RT"):
            #print( "RETWEET")
            continue
        
        words= tw.split(" ")
        toremove=[]
        for i,word in enumerate(words):
            #print (str(word))
            if "https" in word or "#" in word or "@" in word:
                words[i]=""
            
        print (" ".join(w for w in filter(lambda x: x!="", words)))

        

    #for tweet in public_tweets:
    #    print (tweet.text)
    return render_template('/main.html')
  