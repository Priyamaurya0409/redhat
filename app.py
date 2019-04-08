from flask import Flask, render_template, request, Response, stream_with_context, jsonify,flash,Markup
import requests
import json
import os
from flask_cors import CORS,cross_origin

"""""""""""""""""""""""""""""""""""""""""""""""
Initialize app, define global variables, etc.
"""""""""""""""""""""""""""""""""""""""""""""""
app = Flask(__name__)
CORS(app)

"""""""""""""""""""""""""""""""""""""""""""""""
Index for checking Microservice is running...
"""""""""""""""""""""""""""""""""""""""""""""""
@app.route("/")
def index():
  return render_template("index.html")
 

if __name__ == "__main__":
  port = int(os.environ.get("PORT",8080))
  app.run(host='0.0.0.0', port=port,debug=True)
