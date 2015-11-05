import requests
import json

class Sentiment:
   def __init__(self, text, ourid, dt):
      self.text = text
      self.ourid = ourid
      self.dt = dt
   #sentilabel, sentiprob
   #profanelabel, profaneprob   

def getAllAnalysis(textlist,datelist):
   
   data = {
   'text_list': textlist
   }

   toret = []

   i = 0
   for t in textlist:
      i = i+1
      s=Sentiment(t,i,datelist[i-1])
      toret.append(s)

   response = requests.post(
   "https://api.monkeylearn.com/v2/classifiers/cl_qkjxv9Ly/classify/?",
   data=json.dumps(data),
   headers={'Authorization': 'Token 337eb618b507a1c8407f8f299327fcf4a14d0de6',
           'Content-Type': 'application/json'})
   
   json1 = json.loads(response.text)
   
   i = 0;
   for x in json1['result']:
      toret[i].sentilabel = x[0]['label']
      toret[i].sentiprob = x[0]['probability']
      i = i +1
   
   response = requests.post(
   "https://api.monkeylearn.com/v2/classifiers/cl_KFXhoTdt/classify/?",
   data=json.dumps(data),
   headers={'Authorization': 'Token 337eb618b507a1c8407f8f299327fcf4a14d0de6',
            'Content-Type': 'application/json'})

   json1 = json.loads(response.text)
   
   i = 0;
   for x in json1['result']:
      toret[i].profanelabel = x[0]['label']
      toret[i].profaneprob = x[0]['probability']
      i = i +1





   return toret


