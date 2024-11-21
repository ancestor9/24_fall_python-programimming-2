# 간단한 HTTP 클라이언트 코드
import requests

# if __name__ == "__main__":
#     response = requests.get("http://localhost:8080")
#     print("Server Response:", response.text)
    

if __name__ == "__main__":
    response = requests.get("https://c8b3-112-169-221-81.ngrok-free.app/")
    print("Server Response:", response.text)