import socket
host='104.141.5.27'
port=5000
s=socket.socket()
s.connect((host,port))
m=raw_input("Press enter to send file -->")
g=open('client.txt','rb')
n=g.read()
while True:
       if m=='exit':
	      s.send(m)
	      data=s.recv(1024)
	      print str(data)
	  break
       else:
          s.send(n)
          data=s.recv(1024)
          print str(data)
          m=raw_input()
s.close()			
