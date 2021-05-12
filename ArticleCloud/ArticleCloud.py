# using https://ainize.ai/bakjiho/GPT2-Article-Large2
import requests
import os

url = "https://main-gpt2-article-large2-bakjiho.endpoint.ainize.ai/api/"
params = {
    'input':'bitcoin'
}
response = requests.get(url, params=params)

path = "./"
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith(".txt")]

if response.status_code == 200:
    res = response.text
    print(res)
    # 파일이 있는지 찾고 있으면 바로 덮어쓰기, 없으면 생성후 작성.
    filename = "source/%s.txt" % params['input']

    f = open(filename, 'w')
    f.write(res)
    f.close()
else:
	print("Failed Request")