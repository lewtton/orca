import os
import time

try:
    with open('prime.txt', 'w', encoding="utf8") as f:
        f.write("this is a test")
        f.write("这是个测试")
        print(type(f))

except expression as identifier:
    pass
 
# file ="‪D:/Test/big_buck_bunny.mp4"

 
# print( os.path.getatime(file) )   # 输出最近访问时间
# print( os.path.getctime(file) )   # 输出文件创建时间
# print( os.path.getmtime(file) )   # 输出最近修改时间
# print( time.gmtime(os.path.getmtime(file)) )  # 以struct_time形式输出最近修改时间
# print( os.path.getsize(file) )   # 输出文件大小（字节为单位）
# print( os.path.abspath(file) )   # 输出绝对路径
# print( os.path.normpath(file) )  # 规范path字符串形式