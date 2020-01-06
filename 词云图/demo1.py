from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
import jieba
import numpy
import PIL.Image as Image
import matplotlib.pyplot as plt
#1.将字符串切分
def chinese_jieba(text):
    wordlist_jieba=jieba.cut(text)
    space_wordlist=" ".join(wordlist_jieba)
    return space_wordlist
with open("ciyuntu.txt" ,encoding="utf-8")as file:
    text=file.read()
    text=chinese_jieba(text)
    #2.图片遮罩层
    # mask_pic=numpy.array(Image.open("dog.png"))

    backgroud_Image = plt.imread('0.jpg')
    #3.将参数mask设值为：mask_pic
    wordcloud = WordCloud(background_color='white',max_words=10000,font_path="C:/Windows/Fonts/simkai.ttf",stopwords=STOPWORDS,mask=backgroud_Image).generate(text)
    image_colors = ImageColorGenerator(backgroud_Image)
    image=wordcloud.to_image()
    image.show()
