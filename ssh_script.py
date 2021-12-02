import socket
import paramiko
from getpass import getpass
import sys
# first we need host and port to get the TCP connection
# and then we need username and password to access the shell
HOST = input("Enter the IP or Domain:")
PORT = 22

# here we make a function to execute the command
def Connect(user,password,cmd,host=HOST,port=PORT):
    client = paramiko.SSHClient()# client is created and further symmetric encryption
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())# loads the missing keys
    client.load_system_host_keys()# loads keys
    try: # handle the error for wrong ip and username pass
        client.connect(host,port,user,password)# connects to the hostname port user and with pass
    except (socket.gaierror,AttributeError,paramiko.SSHException):
        print(f"Your ip {host} or uname {user} is wrong !!")
        sys.exit()
    except paramiko.ssh_exception.NoValidConnectionsError:
        print(f"SSH is not enable in the remote!!!")
        sys.exit()
    stdin , stdout , stderr = client.exec_command(cmd)# deals with error and output
    print(stdout.read().decode('ascii'),stderr.read().decode('ascii'),end="\n")
    client.close()

if __name__ == "__main__":
    user =  input("Enter you Username:")
    password = getpass(prompt="Password:") # just a temporary password
    cmd = ""
    if not password:
        sys.exit("Password is not given!!!")
    while cmd != "exit":
        cmd = input("Enter Command:")
        Connect(user,password,cmd)


