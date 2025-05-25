import datetime

def log_event(message: str):
    timestamp = datetime.datetime.now().isoformat()
    with open("logs.txt", "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(f"[LOG] {message}")
