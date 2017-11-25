import http.client, urllib.parse, json

sentence = input()
wordcount = len(sentence.split())
print(wordcount)
params = {'mkt': 'en-US', 'mode': 'spell', 'text': sentence}
key = '32ed427d493d4b3da7805d4cb9626855'
host = 'api.cognitive.microsoft.com'
path = '/bing/v7.0/spellcheck'
headers = {'Ocp-Apim-Subscription-Key': key,
'Content-Type': 'application/x-www-form-urlencoded'}
conn = http.client.HTTPSConnection(host)
params = urllib.parse.urlencode (params)
conn.request ("POST", path, params, headers)
response = conn.getresponse()
data = json.load(response)
print(sentence)
tokens = data["flaggedTokens"][0]["offset"]
print(tokens)
score = int(wordcount) - int(tokens)
print("The number of correctly spelt words is: " + str(score) + " out of " + str(wordcount) +"!")
