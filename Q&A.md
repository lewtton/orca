#### 1、安装数据库POSTGRES和python的中间件出错，需提前apt安装postgresql-server-dev-<nn> 包
>apt install postgresql-server-dev-<nn> 
>pg_ctlcluster 11 main start
#### 2、修改nginx.conf后重启服务，提示nginx负载过大，实际是与default冲突
>简单的服务器建议直接删除或注销nginx.conf中include文件

#### 3、使用Python(anaconda)pip安装uwsgi报如下错误:
>lto1: fatal error: bytecode stream generated with LTO version 6.0 instead of the expected 4.1

##### 这是由于gcc版本不一致导致的，网上看到很多解决办法都是改变gcc版本，但改变gcc版本会影响到其他的程序。
##### 如果python是用anaconda 安装，可以用conda的方式安装uwsgi，问题可以解决。
>conda install -c conda-forge uwsgi
##### 有可能碰到 libiconv.so 动态库找不到的问题，同样可以用conda安装
>conda install -c conda-forge libiconv
```
感谢作者：Jlan
链接：https://www.jianshu.com/p/89a16c008898
```
