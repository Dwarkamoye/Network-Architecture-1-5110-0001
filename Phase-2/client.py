import sys
import select
import socket

hostname = '128.171.8.120'
buffer_size = 1024
portnumber = 3000


def client():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        soc.connect((hostname, portnumber))
    except:
        print 'Connection not available'
        sys.exit()

    print 'Connected to remote server'

    while True:
        socketList = [sys.stdin, soc]
        read, write, error = select.select(socketList, [], [])

        for sock in read:
            if sock == soc:
                dataRecv = sock.recv(buffer_size)
                if not dataRecv:
                    print '\nDisconnected from server'
                    sys.exit()
                elif dataRecv == "exit":
                    print ("Server closed connection")
                    sys.exit()
                else:
                    print("Received from server:  " + dataRecv)
            else:
                # user typed a message
                msg = raw_input()
                soc.send(msg.encode("utf8"))


if __name__ == "__main__":
    sys.exit(client())
