# Use flask
from threading import Thread

from flask import Flask

#define flask app
app = Flask('')


#create route for home page
@app.route('/')
def main():
  return "server online!"


#Run our flask app in a thread so that the bot and website can run simultaneously.
def run():
  app.run(host="0.0.0.0", port=8080)


def keep_alive_func():
  server = Thread(target=run)
  server.start()
