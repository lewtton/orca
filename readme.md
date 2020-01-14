# 项目概述
* 根目录下整体为Django项目, 操作系统为Debian 9 GNU/Linux
* 后端环境为Django(动态python服务器)+uWSGI(wsgi中间件)+nginx(静态web服务器)+postgresql(数据库)
* 前端环境为React+bootstrap+jQuery
* 智能家居底层为Crestron中控系统, 使用socket与python汇接
* 无头浏览器使用Puppeteer
## 软件安装以及环境依赖
#### 首先安装
apt install python3 python3-pip virtualenv nginx uwsgi postgresql

#### Python虚拟环境
* 创建并进入虚拟环境目录
>mkdir /opt/pyenv/ && cd !$
* 执行创建虚拟环境命令
>virtualenv  --no-site-packages --python=python3 pyenv3
* 启动虚拟环境
>source /opt/pyenv/pyenv3/bin/activate
* 退出虚拟环境
>deactivate

#### 进入虚拟环境后安装
pip install django requests psycopg2 pandas openpyxl numpy beautifulsoup4
#### 数据库初始化
* 根据Model.py将model层转为迁移文件migration
>python manage.py makemigrations
* 执行迁移文件,更新数据库
>python manage.py migrate
* 查看迁移文件的执行状态
>python manage.py showmigrations
## 配置信息
#### NGINX
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
        
#### uWSGI 
* 配置文件
> ./uwsgi.ini
* 启动命令
> /opt/pyenv/pyenv3/bin/uwsgi -i  /mnt/d/debian/orca/uwsgi.ini        
#### Django
以下文件包括时区, 数据库, 静态文件(图片,js,css...)路径, 模板文件(html文件)路径等相关配置
>./orca/settings.py

#### 前端文件
        ├── static  
        │   ├── assets  
        │   ├── bootstrap  
        │   ├── cache  
        │   ├── image  
        │   └── local  

## 目录结构
        ├── api  
        ├── cache  
        ├── manage.py  
        ├── orca  
        ├── static  
        ├── stocks  
        ├── templates  
        └── uwsgi.ini  
