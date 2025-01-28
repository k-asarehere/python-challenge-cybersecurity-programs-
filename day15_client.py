# a simple TCP client-server application using the socket library

# client logic to connect to server logic

# run the server codes first before the client side in your terminal

import socket 

# create a connection using IPv4 and TCP protocol
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname()
port = 443

# establish the connection with the server
connection.connect((host, port))
print('You are connected to the server successfully!')

# receive the data from the server side
data = connection.recv(1024) # receive up to 1024 bytes(1kb) of data
print('Message received from server:', data.decode())

# close the connection with the server
connection.close()