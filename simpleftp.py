# -*- coding: utf-8 -*-
"""
Spyder Editor
)
This is a temporary script file.
"""
import os
import sys
from ftplib import FTP  
      
ftp = FTP()  
timeout = 30                                             # 防假死时间30秒
port = 21                                                # FTP端口21
ftp.connect('192.168.16.85',port)                       # 连接FTP服务器  
ftp.login('hi','123')                                    # 登录  
print (ftp.getwelcome())                                 # 获得欢迎信息   
Path="Pictures/data/"                                    # FTP路径
ftp.cwd(Path)                                            # 设置FTP路径
ftp.dir()  
list = ftp.nlst()                                        # 获得目录列表  
for name in list:                                        # 建立循环
    print(name)                                          # 打印文件名字  
    DL = "C:\\Users\\Tianyi Xia\\Desktop\\pythonftp\\"   # 下载地址
    LoaclFile = DL+name                                  # 下载文件
    bufsize = 1024  
    file=open(LoaclFile,"wb")  
    ftp.retrbinary('RETR %s' %os.path.basename(LoaclFile),file.write,bufsize) 
ftp.quit()                                               # 退出FTP服务器


#for name in list:
#    if name == "abc.mp4":                                        # 建立循环
#        print(name)                                         # 打印文件名字  
#        DL = "C:\\Users\\Tianyi Xia\\Desktop\\pythonftp\\"   # 下载地址
#        LoaclFile = DL+name                                  # 下载文件
#        bufsize = 1024  
#        file=open(LoaclFile,"wb")  
#        ftp.retrbinary('RETR %s' %os.path.basename(LocalFile),file.write,bufsize) 
##    else:
##        print('abc')
#ftp.quit()                                               # 退出FTP服务器
#
