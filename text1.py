from utils import header
import requests
from lxml import etree
from csv import DictWriter
import os
import  time
# coding:utf-8

has_header = os.path.exists('gushiwen.csv')
header_fields = ('name','author','content')
def itempipline4csv(item):
    global has_header
    with open('gushiwen.csv','a',encoding="utf-8") as f:
        writer = DictWriter(f,header_fields)
        if not has_header:
            writer.writeheader() #写入一行的标题
            has_header = True
        writer.writerow(item)

def get(url):
    resp = requests.get(url, headers={'User_agents': header.get_ua()})
    if resp.status_code == 200:  #Ppython 的判断==，！=，<等 判断状态码进行解析
        parse(resp.text)

    else:
        raise Exception("请求失败")

def parse(html):
    root = etree.HTML(html)  #解析函数获取html的根源数目
    divs = root.xpath('//div[@class = "left"]//div[@class = "sons"]') #取根节点的div下对应标签的属性 list[<Elements>]
    item={}
    for div in divs:
        if len(div.xpath('.//p[1]//text()'))!=0:
            item['name'] = div.xpath('.//p[1]//text()')[0]
            item['author'] = ' '.join(div.xpath('.//p[2]/a/text()'))
            item['content'] = '\n'.join(div.xpath('.//div[@class="contson"]//text()'))
            itempipline4csv(item)

#获取下一页连接 分布式爬虫，拼接url

if __name__ == '__main__':
    base_url = 'https://so.gushiwen.cn/shiwens/default.aspx?page='
    down_url = '&tstr=%e9%80%81%e5%88%ab&astr=&cstr=&xstr='
    n = 5
    for i in range(1, n):
        final_url = base_url + str(i) + down_url
        time.sleep(0.5)
        get(final_url)


print("end:")