from flask import Flask, request, Response, render_template, jsonify
from werkzeug.utils import secure_filename
import requests
import time
import random
# from WordCloud_ENG import *

app = Flask(__name__, static_url_path='/static')

@app.route("/gpt-2", methods=["POST"])
def gpt2():
    input = request.form['input']
    url = "https://main-gpt2-article-large2-bakjiho.endpoint.ainize.ai/api/"
    params = {
        'input': input
    }
    response = requests.get(url, params=params)
    res = response.text
    filename = "static/images/%s.txt" % input
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(res)
    print(res)
    return res

# @app.route("/WordCloud")
# def WordCloud(input):
#     wc.binaryCloud(input)
#     wc.colorCloud(input)

@app.route("/")
def main():
    return render_template("index.html")

@app.route('/news')
def getNews():
   return render_template('news.html', image_file='images/graph01.png')

if __name__ == "__main__":
    from waitress import serve
    serve(app, host='0.0.0.0', port=4000)