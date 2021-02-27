import fn

if __name__ == '__main__':
    # client setting
    host = 'dormroom.myddns.me'  # 182.234.92.165
    port = 17001
    max_transfer_speed = 1024
    password = 'jameslu'

    # massage
    request = 'start'
    fn.socket_model( host=host, port=port ).socket_client( request=request, type='msg', pwd=password )

    # key logger
    # fn.socket_model(host=host, port=port).socket_client(request='', type='key_logger', pwd=password)

    # upload
    # request = './record_near_field_20210218.csv'
    # fn.socket_model(host=host, port=port, max_transfer_speed=max_transfer_speed).socket_client(request=request, type='upload', pwd=password, hide_msg=False)

    # download
    # fn.socket_model(host=host, port=port, max_transfer_speed=max_transfer_speed).socket_client(request=None, type='download', pwd=password)