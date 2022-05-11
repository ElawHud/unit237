import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def ping(host):#This line defines ping as a python function, and adds host as an argument to be used within the fuction  
   
    #Returns True if host (str) responds to a ping request.
    #Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
   

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'
    #This adjusts the ping to work between platforms as the ping is fomatted diferently between windows and linux, 
    #to do this it uses the platform command to check the OS the script is being executed on
    #if platform ==windows the line moves on 
    #the else says if windows is not being used include -c this is because the ping command on linux requires -c
    

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '4', host] #here the ping command is constructed the host is the ip address or hostname to be pinged
    #on the line above I put 4 to modify the amount of ping tests performed, the above will perform 4 pings, this is done to ensure reliability 
   
    
    if subprocess.call(command) == 0: #the below nested statement is only executed if the command has been executed 
        msg = 'Ping  ' + host +  ' successfully :)' #outputs a message to say the ping is successfully 
    else:# the else only triggers if the if statment above did not, when else is triggered the below line is executed 
        msg= 'Ping  ' + host +  ' failed :(' #outputs a message saying the ping was unsuccesful 

    return msg #returns the message to the terminal  

host = 'Ass2Container0' #declares the variable host as the hostname of one of my containers 
host1 = '172.21.0.4' #declare the variable host1 as the ip address of a container 
host2 = '172.21.0.5'#declare the variable host1 as the ip address of a container 

print('\n',ping(host),'\n')#this calls the previously defined ping function and excutes the function using the defined host varriable 
#this line will ping Ass2Container0
print('\n',ping(host1),'\n')#this calls the previously defined ping function and excutes the function using the defined host1 varriable
#the line above will ping 172.21.0.4
print('\n',ping(host2),'\n') #this calls the previously defined ping function and excutes the function using the defined host2 varriable
#the line above will ping 172.21.0.5
