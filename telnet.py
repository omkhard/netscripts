import getpass
import sys
import telnetlib

HOST = input("ENter your IP:")

user = input("Enter your remote account: ")

password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")

tn.write(user + "")

if password:
    tn.read_until("Password: ")
    tn.write(password + "")

tn.write("ls")

tn.write("exit")

print(tn.read_all())