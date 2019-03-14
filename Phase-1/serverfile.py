import socket
import os
HOSTNAME='104.141.5.27'
PORTNUMBER=5000
sock=socket.socket()
sock.bind((HOSTNAME,PORTNUMBER))
sock.listen(0)
connect,address=sock.accept()
while True:
           data=connect.recv(16384)
	   if data=='exit':
	     connect.send('Bye Bye Server')
	     break
	   else:
         try:
            fileToWrite=open('server.txt','w')
            if(os.path.isfile('server.txt')):
             fileToWrite.write(data)
             fileToWrite.close()
             print str(data)
             connect.send(data+'\nText Added by the Server')
         except error as e:
            print str(e)

connect.close()
