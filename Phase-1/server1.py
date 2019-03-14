import socket
HOSTNAME='104.141.5.27'
PORTNUMBER=5000
sock=socket.socket();
#with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
sock.bind((HOSTNAME,PORTNUMBER))
sock.listen(0)
connect,address=sock.accept()
#with connect:
print('Client connected is :', address)
while True:
	data=connect.recv(1024)
	if data=='Bye from client Dwarkamoye Mohanty':
	   connect.send('Bye from server Dwarkamoye Mohanty')
	   break
	elif data=='Hello from client Dwarkamoye Mohanty':
        connect.send('Hello from server Dwarkamoye Mohanty')
        print str(data)
    else:
        print str(data)
        connect.send(data)
connect.close()	   
