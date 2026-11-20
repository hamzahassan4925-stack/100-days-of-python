import time
from urllib.parse import quote
import requests

username = "resi_337afc7b"
password = quote("Z4Bpig~XnT+_")
proxy_url = f"http://{username}:{password}@pr.oxylabs.io:7777"

proxies = {
    "http": proxy_url,
    "https": proxy_url,
}

for i in range(5):
    try:
        r = requests.get("https://httpbin.org/ip", proxies=proxies, timeout=20)
        ip = r.json().get("origin")
        print(f"Attempt {i + 1} -> IP: {ip}")
    except Exception as e:
        print(f"Attempt {i + 1} -> Error: {e}")
    time.sleep(1)