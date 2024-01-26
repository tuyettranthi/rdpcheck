import random
import time

def generate_ip():
    ip = ""
    for _ in range(4):
        ip += str(random.randint(0, 255)) + "."
    return ip[:-1]

ports = [3389, 5900, 80, 443, 8080, 8000]
ip_count = 50000
creation_speed = 0.0

with open("proxy.txt", "w") as file:
    for _ in range(ip_count):
        ip = generate_ip()
        for port in ports:
            file.write(f"{ip}:{port}\n")
        time.sleep(creation_speed)