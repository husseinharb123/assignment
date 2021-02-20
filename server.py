import socket
import time

date =("time.ctime() : %s" % time.ctime())[14:]   # local time and date     ## source stackoverflow


local_ip = "127.0.0.1"  # server address
port = 7210     # port mumber
receive_buffer_size = 4094 # size

mysocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) # create  UDP socket for server

mysocket.bind((local_ip, port)) # bind the socket 


while True:
    message, address_client = mysocket.recvfrom(receive_buffer_size)  #recive from client 
   
    print (f"Date : {date}") # print local time and date 
    
    if message:
        mysocket.sendto(message, address_client)  #resend the recieved message 
        
        
# source : i have used the slides and book 
