import fn

def register(pwd):
    pwd = fn.tool().pwd2encode(pwd, 'SHA')
    pwd = fn.tool().pwd2encode( pwd, 'MD5' )
    return pwd

if __name__ == '__main__':

    # filter password (double encryption: MD5+SHA1)
    # print(register('your_password'))
    filter_PWD, pwd_whitelist = True, []
    pwd_whitelist.append('bced97bf50c8726c975489fbbeed3c62')

    # server setting
    port = 7001
    channel_max = 5
    max_transfer_speed = 999999999  # byte/s

    # start the server
    fn.socket_model(host='10.1.200.94', port=port, max_transfer_speed=max_transfer_speed).socket_server(channel_max=channel_max, filter_PWD=filter_PWD, pwd_whitelist=pwd_whitelist)
