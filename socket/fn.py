import socket
import struct
from datetime import datetime
import threading
import time, os
from tqdm import tqdm, trange
import json
import pickle
import hashlib

class tool(object):

    def __init__(self):
        pass

    def pwd2encode(self, pwd, type=None):
        if type == 'MD5':
            m = hashlib.md5()
            m.update( pwd.encode( "utf-8" ) )
            pwd = m.hexdigest()
        if type == 'SHA':
            m = hashlib.sha1()
            m.update( pwd.encode( "utf-8" ) )
            pwd = m.hexdigest()
            print(pwd)
        return pwd

class socket_model(object):

    def __init__(self, host, port, max_transfer_speed=1024):
        self.max_transfer_speed = max_transfer_speed
        self.host = host
        self.port = port

    def common_filter(self, whitelist, candidate, encode=None):
        candidate = tool().pwd2encode(candidate, encode)
        validation_results = False
        if candidate in whitelist:
            validation_results = True
        return validation_results

    def socket_server(self, channel_max, filter_PWD, pwd_whitelist):
        try:
            s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
            s.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
            s.bind( (self.host, self.port) )
            s.listen( channel_max )
        except socket.error as msg:
            print( msg )
            sys.exit( 1 )
        while True:
            print('', '\n')
            print('Server Online...')
            try:
                conn, addr = s.accept()
                vert_pwd = True
                # password filter
                pwd = conn.recv( 1024 ).decode()
                if filter_PWD is True:
                    vert_pwd = self.common_filter( pwd_whitelist, pwd, encode='MD5')
                conn.send( str(vert_pwd)[0].encode() )
                print( 'Pwssword security verification: ', vert_pwd )
                if vert_pwd:
                    print('Pass security verification!')
                    t = threading.Thread( target=self.deal_data, args=(conn, addr) )
                    t.start()
                else:
                    print('Login block: ', addr[0], '\n' )
                    conn.close()
            except:
                print('Attack form ', addr[0])

    def deal_data(self, conn, addr):
        ti = time.time()
        # progress = tqdm( total=100 )
        print( 'Accept new connection from {0}'.format( addr ) )
        # conn.settimeout(500)
        type = conn.recv(1024).decode()
        print(type)
        if type == 'AIT':
            time.sleep(1)  # load model
            image_type = ['.bmp', '.jpg', 'png']
            conn.send(str(True)[0].encode())
            while True:
                image_path = conn.recv(1024).decode()
                print(image_path)
                if os.path.isfile(image_path) and os.path.splitext(image_path)[1] in image_type:
                    import cv2
                    img = cv2.imread(image_path)
                    time.sleep(1)  # load model
                    # cv2.imshow('img', img)
                    # cv2.waitKey(1000)
                    # cv2.destroyAllWindows()
                    conn.send(str(True)[0].encode())
                else:
                    conn.send(str(False)[0].encode())
        conn.close()
        tf = time.time()
        print('Runtime = ', tf-ti, '[s]', '\n' )
        print( '' )


