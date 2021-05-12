# using https://ainize.ai/bakjiho/GPT2-Article-Large2
import requests

url = "https://main-gpt2-article-large2-bakjiho.endpoint.ainize.ai/api/"
params = {
    'input':'bitcoin'
}
response = requests.get(url, params=params)

if response.status_code == 200:
    res = response.text
    print(res)
else:
	print("Failed Request")