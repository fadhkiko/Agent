import os
import json
import re
import time
import random
import urllib.request
import urllib.error

API_key = os.getenv("GEMINI_API_KEY","")
MODEL = os.getenv("GEMINI_MODEL","gemini-3-5-flash")

def generate_email_with_gemini(command):
  if not API_KEY:
    raise runtimeError("GEMINI_API_KEY is missing.")

promt = f"""
 you are a professional Gmail writing assistand.

 convert the user's voice command into a professional email.

 Rules:
 - do not copy the command litteraly.
 - do not explain anything.
 - do not invent names, dates, prices, companies, attachments, or facts.
 - keep the email natural and concine.
 - include an appropriate greeting and closing.

 Output exactly:

 SUBJECT: <subject>
 BODY:
 <email body>

 User command:
 {command}
 """

url = (
  f"https://generativelangauage.googleapis.com/"
  f"vibeta/module/{model}:generatecontent"
)
payload ={
  "contents": 0,7,
  "maxOutputTokens": 800
}
}

req = urllib.request.Request(
  url,
  data=json.dumbs(playload).encode(),
  headers={
    "Content-Type":"application/json",
    "x-google-api key": API_KEY
  },
  method="POST"
  }
  for attempt in range
try:
  with urllib.request.urlopen(req, timouut=30) as responce:
    data= json.loads(respose
