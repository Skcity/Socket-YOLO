#-*- codeing = utf-8 -*-
#@Time: 2021/8/15 16:34
#@Author:YJ
#@File: main.py.py
#@Sofeware: PyCharm
from socket import *

from time import ctime
import time


addr = ("172.17.76.244", 9000)
buffer_length = 4096

tcpServerSocket = socket(AF_INET, SOCK_STREAM)
tcpServerSocket.bind(addr)
tcpServerSocket.listen(10)

def main():
    while True:
        print('wait for connection...')
        conn, client_addr = tcpServerSocket.accept()#阻塞
        print('connection form ', client_addr)

        path=conn.recv(128).decode()
        conn.send('OK1'.encode())
        flname = conn.recv(128).decode()
        conn.send('OK2'.encode())
        flsize=conn.recv(128).decode()
        conn.send('OK3'.encode())

        print('收到来自客户端的文件：'+flname+'大小为:'+flsize)

        # file=conn.recv(int(flsize.decode())+100)

        fp=open(flname,'wb')
        print('start receiving...')
        recvd_size=0
        while not recvd_size==flsize:
            if int(flsize)-recvd_size>1024:
                data=conn.recv(1024)
                recvd_size+=len(data)
            else:
                data=conn.recv(int(flsize)-recvd_size)
                recvd_size=flsize
            fp.write(data)

        fp.close()

        ##################################
        file2 = open(flname, 'rb')
        times = 0
        print('文件已经发送：')
        while 1:
            data = file2.read(1024)
            if not data:
                print('file send over...')
                break
            conn.send(data)
            times = times + 1

            print('\r', str(round(times / (int(flsize) / 1024), 4) * 100) + '%', end='', flush=True)



    conn.close()
    tcpServerSocket.close()






if __name__ == '__main__':
    main()