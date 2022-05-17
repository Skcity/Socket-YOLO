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

        while True:
            recved=conn.recv(buffer_length)#阻塞
            if not recved:
                break
            info=recved.decode()
            print(f'来自客户端>>{info}')
            toSend = input('请输入>>')
            if(toSend=='exit'):
                break
            bit=conn.send(f'{toSend}'.encode())
            print(bit)

    conn.close()
    tcpServerSocket.close()






if __name__ == '__main__':
    main()