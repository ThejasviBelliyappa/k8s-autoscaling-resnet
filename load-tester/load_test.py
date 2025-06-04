import requests
import threading
import time

def send_query(image_path, url):
    with open(image_path, 'rb') as img:
        start = time.time()
        requests.post(url, data=img.read())
        latency = time.time() - start
        print(f"Latency: {latency:.4f}s")

def load_test(url, image_path, rps, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        threads = [threading.Thread(target=send_query, args=(image_path, url)) for _ in range(rps)]
        [t.start() for t in threads]
        [t.join() for t in threads]
        time.sleep(1)
