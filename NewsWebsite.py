#-*- coding utf-8 -*-
from goose3 import Goose
from goose3.text import StopWordsChinese
import requests
from lxml import etree

class NewsWebsite():
    def __init__(self, Baiduurl):
        self.Baiduurl = Baiduurl

    def getSource(self):
        source_list = []
        for url in self.Baiduurl:
            req_header = {
                'User-Agent': 'Chrome',
                }
            req = requests.get(url, headers = req_header)
            req.encoding = 'utf8'
            html = req.text
            tree = etree.HTML(html)
            source = tree.xpath('//div[@class="date-source"]/a/text()')
            source = ''.join(source)
            source_list.append(source)
        return source_list

    def getTime(self):
        time_list = []
        for url in self.Baiduurl:
            req_header = {
                'User-Agent': 'Chrome',
                }
            req = requests.get(url, headers = req_header)
            req.encoding = 'utf8'
            html = req.text
            tree = etree.HTML(html)
            time = tree.xpath('//div[@class="date-source"]/span[@class="date"]/text()')
            time = ''.join(time)
            time_list.append(time)
        return time_list
    
    def gooseChineseExample(self):
        
        data_list = []
        # 文章地址
        num = 0
        for url in self.Baiduurl:
            # 初始化，设置中文分词
            g = Goose({'stopwords_class': StopWordsChinese})
            # 获取文章内容
            article = g.extract(url = url)
            # 获取标题
            title = article.title
            data_list.append('标题: ' + title)
            # 获取来源
            source = self.getSource()
            data_list.append('来源: ' + str(source[num]))
            # 发布时间
            Time = self.getTime()
            data_list.append('发布时间: ' + str(Time[num]))
            # 显示正文
            text = article.cleaned_text
            data_list.append('文本: ' + text)
            data_list.append('=============================================================================')
            num += 1
        data_list = '\n'.join(data_list)   
        print(data_list)

    def run(self):
        try:
            self.gooseChineseExample()
            print('Success!')
        except:
            print('Failed!')

            

if __name__ == '__main__':
    Baiduurl = ['http://news.sina.com.cn/o/2018-12-30/doc-ihqhqcis1579760.shtml', 'http://finance.sina.com.cn/roll/2018-12-30/doc-ihqfskcn2658387.shtml', 'http://www.qh.gov.cn/zwgk/system/2018/12/31/010320922.shtml']
    Website = NewsWebsite(Baiduurl)
    Website.run()
