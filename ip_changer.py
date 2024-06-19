import subprocess
import time
import random
import socket
import os

os.system('figlet -f slant -c "Random_ip" | lolcat && figlet -f digital -c "Make Py BlackCrow" | lolcat')

def change_ip():
    new_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    subprocess.run(["sudo", "ifconfig", "eth0", "down"])
    subprocess.run(["sudo", "ifconfig", "eth0", "hw", "ether", "00:11:22:33:44:55"])
    subprocess.run(["sudo", "ifconfig", "eth0", "up"])
    subprocess.run(["sudo", "ifconfig", "eth0", "inet", new_ip])

def get_current_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        current_ip = s.getsockname()[0]
    except Exception:
        current_ip = '127.0.0.1'
    finally:
        s.close()
    return current_ip

while True:
    current_ip = get_current_ip()
    change_ip()
    new_ip = get_current_ip()

    print(f"Old IP: {current_ip} | New IP: {new_ip} | Make By Black Crow")
    time.sleep(10)
