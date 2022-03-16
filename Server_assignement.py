#two lines of imports one for ot one for socket
import math, random

import socket
s = socket.socket() 

port = 7777
host = "127.0.0.1"

s.bind((host,port))
print ("socket binded to %s" %(port))

s.listen(5)
print ("socket is listening ")



# function to generate OTP
def generateOTP() :
 
    # Declare a digits variable 
    # which stores all digits
    digits = "0123456789"
    OTP = ""
 
   # length of password can be changed
   # by changing value in range
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
 
    return OTP

while True:
    c, addr = s.accept()
    print ("got connection from ", addr)
    
    c.send("thank you for connecting".encode())
    
    c.close()
    
    break
