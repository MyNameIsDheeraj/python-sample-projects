
import socket
# import subprocess
import sys
from datetime import datetime


target = input ("Enter the IP address: \n")

def port_scan(target):
    try:
        ip = socket.gethostbyname(target)
        
        print(f"Scanning the IP address: {ip}")
        print("Time started: ", datetime.now())
        
        for port in range(1, 100):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            
            if result == 0:
                print(f"Port {port}: Open")
            sock.close()
            
    except socket.gaierror:
        print("Hostname could not be resolved.")
        
    except socket.error:
        print("Couldn't connect to the server.")
    
    except KeyboardInterrupt:
        print("\nYou pressed Ctrl+C.")
        sys.exit()
        
        
port_scan(target)