import requests
import os
url = "http://uav.xinhuanet.com/titlepic/12990/129902843_1530168874124_title0h.jpg"
root_dir    = "D:/Test/image/"
p       = root_dir + url.split('/')[-1]
print(url)
print(p)
try:    
    if not os.path.exists(root_dir):
        os.mkdir(root_dir)
        print("创建文件夹")
    else:
        print("文件夹已存在")        
    if not os.path.exists(p):
        r   = requests.get(url)
        print(r.status_code)
        r.raise_for_status

        # print(len(r.content))
        #print(root)
        with open(p,'wb') as fo:
            fo.write(r.content)
            fo.close()
            print("文件已经保存")
    #print(r.text[1000:1500])    
    else:
        print("文件已经存在")
    #print(r.text[1000:1500])
except:
    print("爬取失败")