from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask_assets import Environment, Bundle
import tweepy

import http.client, urllib.request, urllib.parse, urllib.error, base64
import json


app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '045f300f774941f986881338f7b42196',
}
noTweets=5

@app.route('/')
def main_page():
    #fetch twitter data


    auth = tweepy.OAuthHandler("4demSjUhdVopc5p2IH1rlZPI9", "c3zPuNUjOvfreAxIdwgPTbsx3OJnvNY595VC0lmbs09PcNUtgm")
    auth.set_access_token("391666744-uoByvtlyK64IYKQGiNJO7St7rl1TnGUfRDggdYua", "D0VqdC8iXW0N6YEJLPk6YYYsmiSe29p7hgSvFiBaGEAXI")

    api = tweepy.API(auth)

    #how to you compare to friends api.friends
    user= "BecksTSimpson" #"hacksmiths"#
    public_tweets = api.user_timeline(id=user,count=noTweets)
    
    #print str(public_tweets[0])
    tweetInformation=[]

    for i, tweet in enumerate(public_tweets):
        tweetInformation.append([])
        tw=str(tweet.text) #created_at
        tweetInformation[i].append(str(tweet.created_at))
        tweetInformation[i].append(str(tweet.text))
        
        #print(tweet)
        #print (tw[0:2])
        if(tw[0:2]== "RT"):
            #print( "RETWEET")
            continue
        
        words= tw.split(" ")
        toremove=[]
        for u,word in enumerate(words):
            #print (str(word))
            if "https" in word or "#" in word or "@" in word:
                words[u]=""
            
        twitterPost= " ".join(w for w in filter(lambda x: x!="", words))
        print("twitterPost:  ", twitterPost)
    #wINDOWS LANGUAGE DETECT
    #https://[location].api.cognitive.microsoft.com/text/analytics/v2.0/languages[?numberOfLanguagesToDetect]



        body={ "documents": [{ "id": "string","text":"hello"}]}
        data_json = json.dumps(body)    
        try:
            conn = http.client.HTTPSConnection('northeurope.api.cognitive.microsoft.com')
            conn.request("POST", "/text/analytics/v2.0/languages", data_json, headers)
            response = conn.getresponse()
            data = response.read()
            data= json.loads(data)
            #print(data)
            langType=data["documents"][0]["detectedLanguages"][0]["name"] #langage type
            tweetInformation[i].append(langType)
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))


    print (tweetInformation)

    #for tweet in public_tweets:
    #    print (tweet.text)
    return render_template('/main.html', tweetData=tweetInformation)
  