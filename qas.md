安装数据库POSTGRES和python的中间件出错，需提前apt安装postgresql-server-dev-<nn> 包
>apt install postgresql-server-dev-<nn> 

修改nginx.conf后重启服务，提示nginx负载过大，实际是与default冲突
>简单的服务器建议直接删除或注销nginx.conf中include文件

uwsgi + django(anaconda)安装出错,使用如下
>conda install -c conda-forge uwsgi
