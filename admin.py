import urllib.request #爬虫
import requests
import os,time
from bs4 import BeautifulSoup
def get_HTML(url):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"}
    try:
        r = requests.get(url,timeout = 30,headers=header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding #指定编码形式
        return r.text
    except:
        return "please inspect your url or setup"
#主程序
def runs():
    '''
    url = "http://www.baidu.com"
    #方法01
    data = urllib.request.urlopen(url).read()
    #print(data)
    #将网页放入一个文件
    filepath = "D:/1.html"
    file=open("D:/1.html",'wb')
    file.write(data)
    file.close()
    print(data)
    '''
    #方法02
    url="https://scrm.miaoxing100.com/api/code?randomStr=59411655870245066"
    text = get_HTML(url)
    soup = BeautifulSoup(text,"html.parser")#解析text中的HTML
    # marks = soup.find_all('p',class_='emptySearchErrMsg')
    # marks = soup.find_all('img')
    print(soup)
    #marks=soup.findAll(id="SearchTerm")
    #print(marks)
#程序主方法
if __name__=="__main__":
    runs()