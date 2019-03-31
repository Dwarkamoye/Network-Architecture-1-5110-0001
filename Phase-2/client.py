import sys
import socket
import select

hostname = '128.171.8.120'
buffer_size = 1024
portnumber = 3000
 
def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     
    try :
        s.connect((hostname, portnumber))
    except :
        print 'Connection not available'
        sys.exit()
     
    print 'Connected to remote server'
     
    while 1:
        socket_list = [sys.stdin, s]
         
        # Get the list sockets which are readable
        ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
         
        for soc in ready_to_read:
            if soc == s:
                # incoming message from server, s
                data = soc.recv(buffer_size)
                if not data :
                    print '\nDisconnected from server'
                    sys.exit()
                elif data == "exit":
                    print ("Server closed connection")
                    sys.exit()
                else :
                    print("Received from server:  "+data)
            else :
                # user typed a message
                msg = raw_input()
                s.send(msg.encode("utf8"))

if __name__ == "__main__":
    sys.exit(client())
