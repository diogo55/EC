import socket
import os

def startserver():
    sock = socket.socket(socket.AF_INET, 
                        socket.SOCK_STREAM)
    server_address = ('127.0.0.1',9999)
    sock.bind(server_address)
    
    sock.listen(1)
    
    while True:
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print('connection from', client_address)
        
            while True:
                data = connection.recv(16)
                print('received {!r}'.format(data))
                if data:
                    print('send')
                    connection.sendall(data)
                else:
                    print('no data')
                    break
        finally:
            connection.close()
    
startserver()