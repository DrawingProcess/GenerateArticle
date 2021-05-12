import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud
from wordcloud import STOPWORDS
from wordcloud import ImageColorGenerator
plt.rc('font', family='Malgun Gothic')

# ---------- graph01.png : 흑백 이미지 ----------------
# Image.open(파일명) : 이미지 파일을 연다
image_file = 'source/alice.png'
img_file = Image.open(image_file)
alice_mask = np.array(img_file)
# print(alice_mask)
plt.figure(figsize=(8,8))
plt.imshow(alice_mask, interpolation='bilinear')
plt.axis('off') # 축을 다 없앰
filename = 'source/graph01.png'
plt.savefig(filename)

# ---------- graph02.png : 흑백 이미지 위에 워드클라우드 ----------------
mystopwords = set(STOPWORDS)
mystopwords.add('said')
mystopwords.update(['hahaha','hohoho'])
# print(len(mystopwords))

# 워드클라우드 객체 생성시 여러가지 속성들
# max_words=숫자 : 보여주고자 하는 단어의 최대수
# mask=이미지 배열값 : 배경으로 할 이미지 (array형태여야 함)
wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask, stopwords=mystopwords)
stevefile = 'source/bitcoin.txt'
myfile = open(stevefile, 'rt', encoding='utf-8')
text = myfile.read()
wc = wc.generate(text)
plt.figure(figsize=(12,12))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
filename = 'source/graph02.png'
plt.savefig(filename)

# ---------- graph03.png : 컬러 이미지 위에 워드클라우드 ----------------
image_color_file = 'source/alice_color.png'
alice_color_mask = np.array(Image.open(image_color_file))

# max_font_size=40 : 가장 큰 숫자의 최대 사이즈가 40
# random_state=42 : 랜덤의 시드 값. 값에 따라서 글자의 위치를 고정시켜줌.
wc = WordCloud(background_color="white", max_words=2000, mask=alice_color_mask, stopwords=mystopwords,
max_font_size=40, random_state=42)
wc = wc.generate(text)
plt.figure(figsize=(12,12))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')

filename = 'source/graph03.png'
plt.savefig(filename)

# ---------- graph04.png : 컬러 이미지 ----------------
plt.figure(figsize=(12,12))
plt.imshow(alice_color_mask, interpolation='bilinear')
plt.axis('off')

filename = 'source/graph04.png'
plt.savefig(filename)

# ---------- graph05.png : 컬러 이미지의 색깔에 맞춰 워드클라우드 ----------------
# ImageColorGenerator : 컬러 이미지 배열값의 컬러값을 가져옴
image_color = ImageColorGenerator(alice_color_mask)

# recolor(color_func=이미지컬러제너레이터 객체) : 워드 클라우드를 그릴 새로운 색상을 적용!
newwc = wc.recolor(color_func=image_color, random_state=42)
plt.imshow(newwc, interpolation='bilinear')
plt.axis('off')

filename = 'source/graph05.png'
plt.savefig(filename)

# ---------- graph06.png : 컬러 이미지 위에 색깔에 맞춰 워드클라우드 ----------------
wc = WordCloud(background_color="rgba(255, 255, 255, 0)", mode="RGBA", max_words=2000, mask=alice_color_mask, stopwords=mystopwords,
max_font_size=40, random_state=42)
wc = wc.generate(text)
plt.figure(figsize=(12,12))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')

plt.figure(figsize=(12,12))
plt.imshow(alice_color_mask, interpolation='bilinear')
plt.axis('off')

# ImageColorGenerator : 컬러 이미지 배열값의 컬러값을 가져옴
image_color = ImageColorGenerator(alice_color_mask)

# recolor(color_func=이미지컬러제너레이터 객체) : 워드 클라우드를 그릴 새로운 색상을 적용!
newwc = wc.recolor(color_func=image_color, random_state=42)
plt.imshow(newwc, interpolation='bilinear')
plt.axis('off')

filename = 'source/graph06.png'
plt.savefig(filename)