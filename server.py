import socket, _thread
from random import randrange

def igrac(s):
    a=[] 
    i = 0
    red = 1
    while i < 16:
        br = randrange(0,2)
        a.append(br)
        if (br == 1):
            a.append(0)
        else:
            a.append(1)
        print("%d: %d %d" % (red, a[i], a[i+1]))
        i += 2
        red += 1
    tekst = "You have 3 lives and 8 rows of glass to cross. Each of the rows is made from one regular glass and one tempered glass. The regular glass breaks. Good luck!"
    s.send(tekst.encode())
    brzivoti = 3
    br = 0
    while brzivoti > 0 and br < len(a):
        pole = s.recv(1024).decode()
        if (pole == "l"):
            print("levo")
            if (a[br] == 0):
                brzivoti -= 1
                if brzivoti == 0:
                    tekst = "No more lives left."
                else:
                    tekst = "You stepped on regular glass. Number of lives left: " + str(brzivoti) 
                s.send(tekst.encode())
                br += 2
            else:
                br += 2
                if br == len(a):
                    tekst = "You have successfully reached the end."
                else:
                    tekst = "Good choice. The glass you stepped on was tempered."
                s.send(tekst.encode())
        else:
            print("desno")
            br += 1 
            if (a[br] == 0):
                brzivoti -= 1
                if brzivoti == 0:
                    tekst = "No more lives left."
                else:
                    tekst = "You stepped on regular glass. Number of lives left: " + str(brzivoti) 
                s.send(tekst.encode())
                br += 1
            else:
                br += 1
                if br == len(a):
                    tekst = "You have successfully reached the end."
                else:
                    tekst = "Good choice. The glass you stepped on was tempered." 
                s.send(tekst.encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 1245))
s.listen(5)
while True:
    conn, addr = s.accept()
    _thread.start_new_thread(igrac,(conn,))