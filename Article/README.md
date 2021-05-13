# Generate Article

[Generate Article](https://kubecon-tabtab-jeong-hyun-su.endpoint.ainize.ai/) | [Generate Article](https://github.com/Jeong-Hyun-Su/tabtab) | [Generate Article on Ainize](https://ainize.ai/Jeong-Hyun-Su/tabtab?branch=kubecon)

## Prerequired 

- python3

### Generate Article
Generate Article maked simply rather then TabTab. but It have a same flask server and well done!

#### Usage
```bash
$ pip install -r requirements.txt
$ python3 server.py
```

### Request example to Ainize API 
If you don't know how to use requests, It will help you. 
```bash
$ pip install requests
$ python3 requests_example.py
```

+ Article.py 
Article title to Article context using API GPT2-Article-Large2
+ ArticleCloud.py 
Article title to Article context using API GPT2-Article-Large2 && Generate WordCloud using Article context