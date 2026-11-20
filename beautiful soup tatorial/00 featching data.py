import os
from urllib.parse import quote
import requests


def fetchAndSaveToFile(url, path, proxy_url=None):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    proxies = None
    if proxy_url:
        proxies = {
            "http": proxy_url,
            "https": proxy_url,
        }

    response = requests.get(url, proxies=proxies, timeout=20)
    response.raise_for_status()

    with open(path, "w", encoding="utf-8") as f:
        f.write(response.text)


username = "resi_337afc7b"  #
password = quote("Z4Bpig~XnT+_")  #[cite: 8]
proxy_host = "pr.oxylabs.io"
proxy_port = "7777"

oxylabs_proxy = f"http://{username}:{password}@{proxy_host}:{proxy_port}"

# 1. Pehle IP test karein taake confirm ho jaye ke proxy IP kaam kar rahi hai
fetchAndSaveToFile("https://httpbin.org/ip", "data/my_ip.json", proxy_url=oxylabs_proxy)

# 2. Phir target website fetch karein
target_url = "https://www.lu.lv/en/about-us/ul-media/news/single/t/111029/"
fetchAndSaveToFile(target_url, "data/times.html", proxy_url=oxylabs_proxy)