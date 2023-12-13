# alive.py
from threading import Thread

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
  return "Alive"


def run():
  app.run(host='0.0.0.0', port=8080)


def stay():
  stay = Thread(target=run)
  stay.start()
