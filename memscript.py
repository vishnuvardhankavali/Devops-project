import psutil
import time

while True:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    print("----- Server Health -----")
    print(f"CPU Usage    : {cpu}%")
    print(f"Memory Usage : {memory}%")
    print(f"Disk Usage   : {disk}%")
    print("-------------------------\n")

    time.sleep(5)
