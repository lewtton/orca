# 项目概述
* 根目录下整体为Django项目
* 后端环境为Django(动态python服务器)+uwsgi(wsgi中间件)+nginx(静态web服务器)+postgresql(数据库)
* 前端环境为React+bootstrap+jQuery
* 智能家居底层为Crestron中控系统, 使用socket与python汇接
* 无头浏览器使用Puppeteer

## 配置信息
### nginx
        upstream django {
                server 127.0.0.1:8001;
        }

        server {
                listen  80      default_server;
                server_name     10.10.10.85;
                root    /mnt/d/debian/orca;
                location / {
                        include uwsgi_params;
                        uwsgi_pass django;
                }
                location ^~ /static/ {
                        root /mnt/d/debian/orca;
                }
        }
### Django
orca/settings.py
### 前端文件
├── static
│   ├── assets
│   ├── bootstrap
│   ├── cache
│   ├── image
│   └── local

## 目录结构
.
├── api 
├── cache 
├── manage.py 
├── orca 
├── static 
├── stocks 
├── templates 
└── uwsgi.ini 
