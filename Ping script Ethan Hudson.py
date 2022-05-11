import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '4', host]
   
    
    if subprocess.call(command) == 0:
        msg = 'Ping  ' + host +  ' successfully :)'
    else:
        msg= 'Ping  ' + host +  ' failed :('

    return msg

host = 'AssContainer0'
host1 = '172.21.0.4'
host2 = '172.21.0.5'

print('\n',ping(host),'\n')
print('\n',ping(host1),'\n')
print('\n',ping(host2),'\n')
