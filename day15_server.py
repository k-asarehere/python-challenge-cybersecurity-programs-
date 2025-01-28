# a simple TCP client-server application using the socket library
# server side logic for connecting to client side logic

# run the server codes first before the client side in your terminal

import socket 
# create a connection using IPv4 and TCP protocol
create_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 443 # port number can be any of the port. i chose 443 because it's https-it's a secure web connection protocol 

# listen to a request from a specific ip address and port 
create_connection.bind((host, port))
print(f'Socket connected successfully to device/host: {host}')

# listen to incoming requests from a client 
create_connection.listen(5) # listen to 5 request at a time;refuse if it exceeds that
print('Server is listening.....')

# accept connection from client
while True: # while loop listens to multiple connections,not just one, but it's been ended by the 'break' statement when a connection(with a client) is done
    connection,ip_address = create_connection.accept() # unpack the 2 variables to get the connection variable and the ip address variable
    print('Got a connection from IP address and dynamic port number:', ip_address[0:])
    connection.send('Thanks for connecting to my server :)'.encode())
    connection.close()
    break



