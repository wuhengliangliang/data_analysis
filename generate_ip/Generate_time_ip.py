#定时模拟数据
#coding = UTF-8
#根据课程页面分析拿到数据
#访问的路径
import random

url_paths = [
    "class/112.html",
    "class/128.html",
    "class/145.html",
    "class/146.html",
    "class/131.html",
    "class/130.html",
    "learn/821",
    "course/list"
]

ip_slices = [132,156,124,10,29,167,143,187,30,46,55,63,72,87,98,168]

#随机取样
def sample_url():
    return random.sample(url_paths,1)[0] #随机产生一个



def generate_log(count = 10): #默认10条
    while count >=1:
       query_log = "{url}".format(url = sample_url())
if __name__ == '__main__':
    main()
