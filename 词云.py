import jieba
import wordcloud
import imageio
map1=imageio.imread('四叶草.png')
data = open('弹幕.text',encoding='utf-8')
Content=data.read()
word_list=jieba.lcut(Content)#列表
#列表转字符串
word_str =' '.join(word_list)
#词云图配置
wc=wordcloud.WordCloud(
    width=700,
    height=700,
    mask=map1,
    background_color='white',
    font_path='msyh.ttc',
    stopwords={'了','的'}
)
wc.generate(word_str)
wc.to_file('词云图.png')
#print(word_str)