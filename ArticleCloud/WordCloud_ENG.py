import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud
from wordcloud import STOPWORDS
from wordcloud import ImageColorGenerator
plt.rc('font', family='Malgun Gothic')

def textConfig(stevefile): # stevefile = 'source/bitcoin.txt'
    stevefile = 'source/bitcoin.txt'
    myfile = open(stevefile, 'rt', encoding='utf-8')
    text = myfile.read()
    return text

def binaryCloud(input):
    # ---------- graph01.png : 흑백 이미지 위에 워드클라우드 ----------------
    image_file = 'source/alice.png'
    img_file = Image.open(image_file)
    alice_mask = np.array(img_file)
    mystopwords = set(STOPWORDS)
    mystopwords.add('said')
    mystopwords.update(['hahaha','hohoho'])

    wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask, stopwords=mystopwords)
    stevefile = "./source/%s.txt" % input
    text = textConfig(stevefile)
    wc = wc.generate(text)
    plt.figure(figsize=(12,12))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    filename = 'source/graph01.png'
    plt.savefig(filename)

def colorCloud(input):
    # ---------- graph02.png : 컬러 이미지 위에 워드클라우드 ----------------
    image_color_file = 'source/alice_color.png'
    alice_color_mask = np.array(Image.open(image_color_file))
    
    wc = WordCloud(background_color="white", max_words=2000, mask=alice_color_mask, stopwords=mystopwords,
    max_font_size=40, random_state=42)
    stevefile = "./source/%s.txt" % input
    text = textConfig(stevefile)
    wc = wc.generate(text)
    plt.figure(figsize=(12,12))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    filename = 'source/graph02.png'
    plt.savefig(filename)
    
    # ---------- graph03.png : 컬러 이미지의 색깔에 맞춰 워드클라우드 ----------------
    image_color = ImageColorGenerator(alice_color_mask)
    newwc = wc.recolor(color_func=image_color, random_state=42)
    plt.imshow(newwc, interpolation='bilinear')
    plt.axis('off')
    filename = 'source/graph03.png'
    plt.savefig(filename)

    # ---------- graph04.png : 컬러 이미지 위에 색깔에 맞춰 워드클라우드 ----------------
    wc = WordCloud(background_color="rgba(255, 255, 255, 0)", mode="RGBA", max_words=2000, mask=alice_color_mask, stopwords=mystopwords,
    max_font_size=40, random_state=42)
    wc = wc.generate(text)
    plt.figure(figsize=(12,12))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.figure(figsize=(12,12))
    plt.imshow(alice_color_mask, interpolation='bilinear')
    plt.axis('off')

    image_color = ImageColorGenerator(alice_color_mask)
    newwc = wc.recolor(color_func=image_color, random_state=42)
    plt.imshow(newwc, interpolation='bilinear')
    plt.axis('off')

    filename = 'source/graph04.png'
    plt.savefig(filename)