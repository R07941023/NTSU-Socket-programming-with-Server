import fn

def register(pwd):
    pwd = fn.tool().pwd2encode(pwd, 'SHA')
    pwd = fn.tool().pwd2encode( pwd, 'MD5' )
    return pwd

if __name__ == '__main__':

    # filter_IP
    filter_IP,  ip_whitelist = False, []
    # ip_whitelist.append( '140.112.21.98' )  # NTU Lab425
    # ip_whitelist.append( '115.43.132.160' )  # 中和家
    # ip_whitelist.append( '114.34.214.24' )  # 桃園家

    # filter_mac
    filter_MAC, mac_whitelist = False, []
    # mac_whitelist.append( 'fe80::e92e:5aeb:1bc2:8d75%18' )  # 中和家
    # mac_whitelist.append( 'SDFSDF' )

    # filter password (double encryption: MD5+SHA1)
    # print(register('your_password'))
    filter_PWD, pwd_whitelist = True, []
    pwd_whitelist.append('bced97bf50c8726c975489fbbeed3c62')

    # share the file for client
    share_file = []
    # share_file.append('E:/台灣體育大學/test/version.txt')
    # share_file.append( 'E:/台灣體育大學/test/log.txt' )
    # share_file.append( 'E:/台灣體育大學/test/133221.mp4' )

    # server setting
    port = 7001
    channel_max = 5
    max_transfer_speed = 999999999  # byte/s

    # start the server
    fn.socket_model(host='127.0.0.1', port=port, max_transfer_speed=max_transfer_speed).socket_server(channel_max=channel_max, share_file=share_file, filter_IP=filter_IP, ip_whitelist=ip_whitelist, filter_MAC=filter_MAC, mac_whitelist=mac_whitelist, filter_PWD=filter_PWD, pwd_whitelist=pwd_whitelist)
