import socket

import datetime

if __name__ == '__main__':
    server_address = 'localhost'
    server_port = 4567
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((server_address, server_port))
    sock.listen(1)
    while True:
        # Wait for a connection
        print 'waiting for a connection'
        connection, client_address = sock.accept()
        try:
            print 'connection from', client_address

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(1024)
                print 'received "%s", timestamp: %s' % (data, datetime.datetime.now())
                if data:
                    print 'sending data back to the client'
                    connection.sendall(data)
                else:
                    print 'no more data from', client_address
                    break
        except KeyboardInterrupt:
            print "Got Ctrl+C, closing..."
            connection.close()
            print "Connection closed"
        finally:
            # Clean up the connection
            connection.close()
