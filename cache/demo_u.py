from bs4 import BeautifulSoup
import bs4
import os
import requests

def getHTMLText(url):
    try:
        r=requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def fillUList(ulist, html):
    soup= BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])
def printUlist(ulist, num):
    print("{:^6}\t{:^20}\t{:^10}\t{:^10}\t".format("排名","名称", "地区", "得分"))
    for i in range(num):
        u=ulist[i]
        print("{:^6}\t{:^20}\t{:^10}\t{:^10}\t".format(u[0],u[1],u[2],u[3]))
 
def main():
    ulist=[]
    num=40
    url='http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html=getHTMLText(url)
    #print(html)
    fillUList(ulist, html)
    printUlist(ulist, num)

main()