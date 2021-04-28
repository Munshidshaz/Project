import getpass
import telnetlib

HOST = "192.168.122.166"
user = input("Enter your telnet account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') +b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') +b"\n")

tn.write(b"enable\n")
tn.write(b"pass\n")
tn.write(b"conf t\n")
for i in range (40,50):
        tn.write(b"vlan "+ str(i).encode('ascii')+b"\n")
        tn.write(b"name VLAN_"+str(i).encode('ascii')+b"\n")

tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
