import requests,os,sys,re
from bs4 import BeautifulSoup
url_base = "https://www.meijumi.net/26623.html"
kv  = {"user-agent":"Mozilla/5.0"}
kw  = {"wd":"1999"}
data="下载列表\n"
for i in range(1):

    try:
        # url=url_base+str(i)
        url = url_base
        print(url)
        r   = requests.get(url, headers = kv)
        # print(r.raise_for_status)
        # print(r.request.headers)
        # print(r.encoding)
        # str = {"asdasd","55555555","我是"}
        soup = BeautifulSoup(r.text, "html.parser")
        # mydivs = soup.findAll("div", {"class": "rinfo tdown"})[0].findAll("a")
        code = soup.find_all("a", href=re.compile("ed2k:"))
        # code = soup.prettify().encode("utf8")
        # data = "love u"
        # print(type(data))
        # print(data)
        # data =data + "第"+str(i+1)+"集""\n"
        # data =data + code[0]["href"] + "\n\n"
        # print(str(i+1)+":s:"+type(soup)+"  c:"+type(code)+"\n")
        for ed2k in code:
                print(ed2k["href"])


    except:
        print("Unexpected error:", sys.exc_info()[0])


with open('cache1.html', mode='w', encoding='utf8') as f:
    f.write(data)