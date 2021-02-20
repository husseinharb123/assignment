import socket 
from datetime import datetime

request_string= "hi my name is hussein harb "  # messsage to be sent 
serverip = str(input("Enter the IP address of the server : ") )   # server adddress                    
serverPort =int(input("Enter the port number  of the server : ")   )  # server port number 

clientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) # create UDP socket of client 

RTT_total=0
i =0
for i in range(5): # sending message  5 times
   
    start = datetime.now()  # start couting 
    clientSocket.sendto(request_string.encode(),(serverip, serverPort))
    recmsg, serverAddress = clientSocket.recvfrom(4094)
    end = datetime.now() # end counting ## source stackoverflow
    
    RTT = end - start  #roundtrip time
    time = int(RTT.microseconds)  # time in microsecond   ## source stackoverflow
    i+=1
    print(f"RTT ({i}) : {time} μs ") # print RTT for each rely/rec pair
    RTT_total+= RTT   #  total RTT 

print(F"AVERGE RTT : {RTT_total / 5} μs ")  # print averge RTT

clientSocket.close()  #close the socket 

# source : i have used the slides and book 


