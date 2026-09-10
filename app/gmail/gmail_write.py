import os
import re
import urllib.parse

CLIENT_EMAIL = os.getnv("CLIENT_EMAIL","")

KEYWORDS = {
  "gmail", "email", "e_mail", "mail".
  "write an email", "send an email","draft an email",
"compose an email", "write mail", "send mail","draft mail",
"compose mail"
}
