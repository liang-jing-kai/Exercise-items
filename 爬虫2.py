import requests
from bs4 import BeautifulSoup
import datetime

headers = {
'cookie':'JSESSIONID=wmBi5kBzscnm4l1_NF260uUuu6-UsLeHIYEDXOcFEtxmwqJtOmYK!606661908!-1224042509; BIGipServervpezEVlz6HE/hUCTqe24Ug=!qPPFG2hjSO3S/LOvLKEpjgU2TcOy4XF0pgiITaS7tf/dVzfsPyp5VVYL0WLpDgWP2snCzeBuNoBE7C0=; BIGipServer/8qfVTTvyGuKbaGqbX3Biw=!i4HNbMPFVL9u4xKvLKEpjgU2TcOy4agxl9E4LaQP95AAbHBpNhDrMjc8qmR32udJ2WmRkyMQP/Hr9g==',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}
cs1 = "江门市辖"
cs2 = "佛山高明"
cs3 = "珠海市辖"
cs4 = "江门新会"
def runs(url):
    var = 1
    while var == 1:
        r = requests.get(url,headers=headers).text
        # print(r)
        soup = BeautifulSoup(r, "html.parser")  # 解析text中的HTML
        marks = soup.find_all(style="font-size: 13px;")
        # marks = marks.find_all()
        # print(marks)
        now_time = datetime.datetime.now()
        print("刷新时间：", now_time)
        s = []
        print("  城市","    考位")
        for mark in marks:
            country_label = mark.find_all('td')
            chengshi = country_label[1].string
            kaowei = country_label[2].string
            if chengshi == cs1 or chengshi == cs2 or chengshi == cs3 or chengshi == cs4:
                print(chengshi,kaowei)
                # s.append(chengshi+kaowei)
        # print(s)


if __name__=="__main__":
    input_url = 'https://www.eeagd.edu.cn/cr/cgbm/xqcx.jsp'
    runs(input_url)