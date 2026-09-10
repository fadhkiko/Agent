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
 -
