import socket

def startclient():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_address = ('127.0.0.1', 9999)
    
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)
    
    try:
        print('U ass')
    
    finally:
        print('closing socket')
        sock.close()

startclient()