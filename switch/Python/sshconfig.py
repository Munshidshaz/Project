import getpass
import telnetlib

user = input("Enter your telnet account: ")
password = getpass.getpass()
#opening ip folder

f = open ('myswitches')

for IP in f:
    IP=IP.strip()
    print ("Configuring "+ (IP))
    HOST=IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    #login in 
    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    #command or work
    tn.write(b"conf t\n")
    tn.write(b"line vty 0 4\n")
    tn.write(b"login local\n")
    tn.write(b"transport input all\n")
    tn.write(b"ip domain-name esoft.lk\n")
    tn.write(b"crypto key generate rsa\n")
    tn.write(b"1024\n")
    tn.write(b"end")
    #exiting 
    tn.write(b"wr\n")
    tn.write(b"exit\n")
    #show output
    print(tn.read_all().decode('ascii'))