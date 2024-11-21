# 간단한 HTTP 서버 코드
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple HTTP server response!")

if __name__ == "__main__":
    server_address = ('', 8080)  # localhost:8080에서 실행
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("HTTP Server running on port 8080...")
    httpd.serve_forever()