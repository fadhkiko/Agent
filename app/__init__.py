import os , urllib.parse , urllib.request , render_templates
from app.youtube import youtube_bp

Gemini_api_key = "Gemini API Key";

def home():
  return render_templates (" index.html")

def create_app():
  appp = Flask(_name_)
app.register_blueprint(youtube_bp, url_prefix="/youtube")

@app.route("/html")
def html():
return rendeer_templates("index.html")

return app;
