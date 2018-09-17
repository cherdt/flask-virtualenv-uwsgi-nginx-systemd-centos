from flask import Flask
from flask import request
from flask_cors import CORS
import nltk.chat
from nltk.chat.util import Chat, reflections
app = Flask(__name__)
CORS(app)

@app.route("/")
def what():
    text = request.args.get('text')
    bot = nltk.chat.eliza
    return bot.eliza_chatbot.respond(text)
