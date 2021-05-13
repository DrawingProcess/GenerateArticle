from flask import Flask, request, Response, render_template, jsonify
from werkzeug.utils import secure_filename
import requests
import time
import random
# from WordCloud_ENG import *

app = Flask(__name__, static_url_path='/static')

@app.route("/gpt-2", methods=["POST"])
def gpt2():
    global input
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
   return render_template('news.html', title=input, image_file='images/graph01.png')

@app.route('/txt')
def read_txt(input):
    f = open('static/images/%s.txt' % input, 'r')
    ## 단 리턴되는 값이 list형태의 타입일 경우 문제가 발생할 수 있음.
    ## 또한 \n이 아니라 </br>으로 처리해야 이해함
    ## 즉 파일을 읽더라도 이 파일을 담을 html template를 만들어두고, render_template 를 사용하는 것이 더 좋음
    return "</br>".join(f.readlines())

if __name__ == "__main__":
    from waitress import serve
    serve(app, host='0.0.0.0', port=4000)