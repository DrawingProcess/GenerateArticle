from flask import Flask, request, Response, render_template, jsonify
import requests
import time
import random

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
    print(res)
    return res


@app.route("/")
def main():
    return render_template("index.html")


if __name__ == "__main__":
    from waitress import serve
    serve(app, host='0.0.0.0', port=8080)   