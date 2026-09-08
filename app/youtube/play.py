import re
import urllib.parse
import urlllib.request

def get_vid(query):

  try:
    encoded = urllib.parse.qoute(query)

url= (
  "http:/www.youtube.com/results"
  "?search query="+encoded
)

request = urllib.request.Request(
  url,
  headers = {
    "user-agent":"mozilla/5.0"
  }                       
  }
data= urllib.request.urlopen(
  request,
  timeout=5
).read().decode()("utf-8",errors="ignore")

ids = re.findall(
  r'"vedioId":"([^"]+)";,
  data
)
return ids[0] if ids else none

except Exception:
return none 

def create_youtube_url(command):

  text = command.lower().strip()

patterns = [
  r"play\s+song\s+(.+)",
  r"play\s+music\s+(.+)"
  r"play\s+(.+)",
  r"youtube\s+(.+)"
]

query = command

for pattern in patterns:
  match = re.search(
    pattern,
    text
  )

if match:

quey=match.group(1)
break
query = query.strip()

vedio.id = get_vid(query)

if not vedio_id:
return none

return(
  "http://www.youtube.com/embed/"
  + vedio_id
  +"?autoplay=1&mute=0"
)
