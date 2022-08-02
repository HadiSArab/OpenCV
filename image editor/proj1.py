from crypt import methods

import requests
from flask import Flask, request, redirect, url_for
from flask import render_template
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/image_api')
def image_api():
    



    return "done"