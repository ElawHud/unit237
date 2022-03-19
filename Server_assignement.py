/#Ethan Hudson 
#Univerity of Sunderland
#Unit 237
#Assignment 1 
#otp generator
#last updated: 19/3/22

#Below is my code for my python server

#two lines of imports one for otp generator one for socket
import math, random #these functiona are imported as they are required to build the One time password generator 

import socket #socket programmming is imported as its functions are required to build functioning server in python 
s = socket.socket()  #this line is used to create a varible of s and defines it as a socket object 

port = 7777 #this line defines the server port number as 7777, 7777 is used because the first 1000 port number are reserved and cannot be used, also 7 is lucky
host = "127.0.0.1" #this line define the host or the server as having the ip address 127.0.0.1
#I used this address as it is the loopback address and I am running the server locally

s.bind((host,port))#this line binds the previously created socket object to the defined host and port number 
print ("socket binded to %s" %(port))#this is simply a print line to print the ip and port info this is used to verify they are configured correctly
#also it is good for reference to have the ip and port info outputted 

s.listen(5)#this command the socket to listen 
print ("socket is listening ")#this print line is used to verify that the server is operational 

#Below is the code i used to provide authentication on the server 
username=input("enter the correct username")#this lines ask the client for a username, the text in quotations is outputted then the user inputs the Username
password=input("enter the correct password")#this lines ask the client for a password, the text in quotations is outputted then the user inputs the Password
#For both username and password the users response is stored in the varible define at the strat of the line so username and password
    
while username != "Ethan":#this is while loop statement != means not equal to so != Ethan is a criteria username is the same varible defined in the previous line 
    username=input("enter the correct username")# so if username is not equal to Ethan the next line is executed 
    #the ext line repeats the line to ask for a username creating a loop 
    #if the username is Ethan idented line of code is skipped and the code moves on to the next line which is line 38
        

while password != "Pa55": #This while statement functions just the same as the previous expects it checks if the input in the password variable is Pa55
    password=input("enter the correct password")# if the above criteia is reached this lines executes, the criteria is the password being wrong 

#with the authentication complete the server moves on to execute the code for the one time password generator, the code for this is below 
#the first defines a funtion as generateOTP so all the code for the OTP is stroed in the function 
def generateOTP() :
 
  
   
    digits = "0123456789" # defines a digit varible with all the avilable numbers for the OTP 
    OTP = "" #otp a varible which stores the digits 
 
   
   
    for i in range(4) : # this line changes the length of th OTP 
        OTP += digits[math.floor(random.random() * 10)] # this line uses the digits to generate a random seqence
 
    return OTP #outputs the OTP 

#below is the code for the server continued this is the final part of the server code so it is put last 
#another while loop, this one keeps the server active by not letting the code finish 
while True:#while the indented code is true
    c, addr = s.accept() #this lines connects the server to the client 
    print ("got connection from ", addr)# a print lines which outputs the info on aconnection to the client 
    #c refers to the client
    c.send("thank you for connecting".encode())# this line encodes the text in the commas to the client 
    
    c.close()#stops sending data to the client 
    
    break # ends the loop 
