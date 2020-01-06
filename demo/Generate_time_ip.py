#定时模拟数据
#coding = UTF-8
#根据课程页面分析拿到数据
#访问的路径
import random
import time

url_paths = [
    "class/112.html",
    "class/128.html",
    "class/145.html",
    "class/146.html",
    "class/131.html",
    "class/130.html",
    "learn/821.html",
    "course/list.html"
]
ip_slices = [132,156,124,10,29,167,143,187,30,46,55,63,72,87,98,168]
#随机取样

http_referers = [
    "https://www.baidu.com/s?wd={query}",
    "https://www.sogou.com/web?query={query}",
    "https://cn.bing.com/search?q=={query}",
    "https://search.yahoo.com/search?p=={query}",
]
search_keyword = [
    "Spark SQL实战",
    "Hadoop基础",
    "Strom实战",
    "Spark Streaming实战",
    "大数据面试"
    "Node.js入门到企业Web开发中的应用"
]
#状态码的生成
status_codes = ["200","404","500"]

#url的随机生成
def sample_url():
    return random.sample(url_paths,1)[0] #随机产生一个
#ip的随机生成
def sample_ip():
    slice = random.sample(ip_slices,4)
    #拼接每次随机产生的四个中的一个来放进去拼接用
    return ".".join([str(item) for item in slice])

#拼接http和搜索内容、
def sample_referer():
    if random.uniform(0,1) > 0.2:
        #如果没有内容就用-代替
        return "-"
    refer_str = random.sample(http_referers,1)
    query_str = random.sample(search_keyword,1)
    return refer_str[0].format(query = query_str[0])
#状态码的自动生成
def sample_status():
    return random.sample(status_codes,1)[0]

def generate_log(count = 10): #默认10条
    #产生当前时间
    time_str = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    while count >=1:
        query_log = "{ip}\t{localtime}\t\"GET /{url} HTTP/1.1\"\t{status}\t{referer}".format(url = sample_url(),ip = sample_ip(),referer = sample_referer(),status= sample_status(),localtime= time_str)
        print(query_log)
        count = count - 1
if __name__ == '__main__':
    generate_log()
