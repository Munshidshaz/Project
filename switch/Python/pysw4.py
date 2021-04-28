import getpass
import telnetlib

user = input("Enter your telnet account: ")
password = getpass.getpass()
#opening ip folder

f = open ('myswitches')

for IP in f:
    IP=IP.strip() #removing spaces
    print ("Configuring Switch "+ (IP))
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
    tn.write(b"terminal length 0\n")
    tn.write(b"show run\n")
    #exiting 
    tn.write(b"exit\n")
    #save output
    readoutput = tn.read_all()
    saveoutput = open ("switch" + HOST,"w")
    saveoutput.write(readoutput.decode('ascii'))
    saveoutput.write("\n")
    saveoutput.close