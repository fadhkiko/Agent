import os
from flask import Flask,request,jsonify, render_templates
from flask_cores import CORS


from app.gmail import(
is_email_command,
extract_email,
create_gmail_url,
generate_email_with_gemini
)

from app.youtube import youtube_bp

def create_app():

    app = Flask(__name__)
    CORS(app)

# youtube
app.register_blueprint(



    return app
