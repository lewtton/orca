## 项目概述
* 服务器操作系统为Debian 9 GNU/Linux
* 静态web服务器:       NGINX
* 后端动态服务器:       Django+uWSGI
* 数据库:              PostgreSQL
* 前端环境:            React+Bootstrap+jQuery
* 智能家居底层为Crestron中控系统, 使用socket与python汇接
* 嵌入式系统使用STM32F103开发板+传感器采集环境信息(温湿度,PM2.5,水浸,烟感等)
* 无头浏览器使用Puppeteer
* 视频编解码使用ffmpeg
* 视频处理使用OpenCV
* 图像识别使用Python pillow包
* 股票查询使用Python Baostock包
* 图表生成使用Chart.js

## C/S工作流程详述
1. 客户端(浏览器,App)发起请求
>可以为`ajax`,只请求部分数据
2. NGINX接受请求, 将请求交由uWSGI处理
>`图片|js|css`等静态请求(URL带`/static/*`标识)直接返回结果,不通过uWSGI
3. uWSGI将请求交由Django处理
>依据`./uwsgi.ini`
4. Django依据路由表分析,交由相应views.py模块
>路由入口文件为`./orca/urls.py`
5. Django下views.py模块执行后台程序
>调取数据库,或者执行其他Python程序
6. Django下views.py回应客户端(浏览器,App)
>根据请求类型,返回`模板页面`, `json数据`, `字典类型数据`

## 软件安装以及环境依赖
#### 首先安装
apt install python3 python3-pip virtualenv nginx uwsgi postgresql

#### Python虚拟环境
* 创建并进入虚拟环境目录
>mkdir /opt/pyenv/ && cd !$
* 执行创建虚拟环境命令
>virtualenv  --no-site-packages --python=python3 pyenv3
* 激活虚拟环境
>source /opt/pyenv/pyenv3/bin/activate
* 退出虚拟环境
>deactivate

#### 进入虚拟环境后安装
pip install django requests psycopg2 pandas openpyxl numpy beautifulsoup4 redis django-redis

#### 数据库初始化
* 根据Model.py将model层转为迁移文件migration
>python manage.py makemigrations
* 执行迁移文件,更新数据库
>python manage.py migrate
* 查看迁移文件的执行状态
>python manage.py showmigrations

## 配置信息
#### NGINX
```
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
```        
#### uWSGI 
* 配置文件
> ./uwsgi.ini
* 启动命令
> /opt/pyenv/pyenv3/bin/uwsgi -i  /mnt/d/debian/orca/uwsgi.ini        

#### Django
以下文件包括时区, 数据库, 静态文件(图片,js,css...)路径, 模板文件(html页面)路径等相关配置
>./orca/settings.py

#### 前端文件
```
├─assets
├─bootstrap
│  ├─css
│  ├─fonts
│  └─js
├─cache
├─image
│  ├─icons
│  └─pics
└─local
└─src
```
## 目录结构
```
├── api
├── cache
├── manage.py
├── orca
├── static
├── stocks
├── templates
└── uwsgi.ini
```
