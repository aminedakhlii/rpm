import requests
import json, os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

INIT = False

def broadcast(situation,location,snap):

  deviceTokens = getTokens()
  serverToken = 'AAAAarnumlk:APA91bE4yfGioJMafya2Zu3Z7F3iCU1Ic4EUaku3CppD5dj6im5S3DC_j8pVYaovEQ0p2e_UfnuPXEbrk_RqdHzWGsHRuICxBJywsl7Ll-yP9RpFjSlYpuzvrCHhStCPm9gJNr1QYHs3'

  headers = {
    'Content-Type': 'application/json',
    'Authorization': 'key=' + serverToken,
  }

  for token in deviceTokens:

    body = {
      'notification': {
        'title': situation + ' Near by!',
        'body': 'Urgent! Someone is having a ' + situation + ' near by\nClick to see location',
        'image': snap
      },
      "data": {
        "click_action": "FLUTTER_NOTIFICATION_CLICK",
        "sound": "default", 
        "status": "done",
        "lat": location['latitude'],
        "long": location['longitude'],
      },
      'to': token,
      'priority': 'high',
    }

    response = requests.post("https://fcm.googleapis.com/fcm/send",headers = headers, data=json.dumps(body))
    print(response.status_code)
    print(response.json())

def initDB():
  global INIT
  if not INIT:
    cred = credentials.Certificate(os.path.dirname(os.path.abspath(__file__)) + '/rpmqa-ca460-firebase-adminsdk-lxjb5-5f28bc627b.json')
    firebase_admin.initialize_app(cred)
    INIT = True

  db = firestore.client()
  return db

def getTokens():
  db = initDB()
  docs = db.collection(u'volunteer_tokens').stream()
  return [doc.get('token') for doc in docs if doc != 'none']