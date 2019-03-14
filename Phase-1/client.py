import socket
HOSTNAME='104.141.5.27'
PORTNUMBER=5000
sock=socket.socket()
sock.connect((HOSTNAME,PORTNUMBER))
message=raw_input("Type  -->")

while True:
       if message == 'Bye from client Dwarkamoye Mohanty':
		   sock.send(message)
		   data=sock.recv(1024)
		   print str(data)
		   break
		   message=raw_input()
       elif message == "Hello from client Dwarkamoye Mohanty":
           sock.send(message)
		   data=sock.recv(1024)
		   print str(data)
		   message=raw_input()
       else:
            sock.send(message)
            data=sock.recv(1024)
            print str(data)

sock.close()		   
