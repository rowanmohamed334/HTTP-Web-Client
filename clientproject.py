import socket
lines=[]
strs=[]
method=''
filename=''
host=''
port=''
with open('inputfile.txt') as f:
 lines=f.readlines()
for line in lines:
 strs=line.split()
 #default port number if it is not given
 if len(strs)==3:
  method,filename,host=strs
  port=80
 #if port number is given
 elif len(strs)==4:
  method,filename,host,port=strs 
 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((host,port))
  if method=='POST':
   #file content
   filecontent=open(f'{filename}')
   content=filecontent.read()
   filecontent.close()
   #compose request packet
   reqpacket=f'{method}/{filename} HTTP/1.0\r\nHost:{host}:{port}\r\n\r\n{content}\r\n'
   #convert packet to byte
   reqb=reqpacket.encode('utf-8')
   s.sendall(reqb)
   respb=s.recv(1024)
  elif method=='GET':
   #compose request packet
   reqpacket=f'{method}/{filename} HTTP/1.0\r\nHost:{host}:{port}\r\n\r\n'
   #convert packet to byte
   reqb=reqpacket.encode('utf-8')
   s.sendall(reqb)
   respb=s.recv(1024)
   #convert recieved byte to string
   resppacket=respb.decode('utf-8')
   resp,data=resppacket.split(f'\r\n\r\n')
   #store data in new file   
   getfile=open(f'{filename}',"w+")
   getfile.write(data)
   getfile.close()
  s.close()
   
    
   
     
