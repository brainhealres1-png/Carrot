import http.server
import socketserver
import os
from pathlib import Path

PORT = 8000
WEB_DIR = Path(__file__).parent / ".web" / "build" / "client"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(WEB_DIR), **kwargs)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super().end_headers()

if __name__ == "__main__":
    os.chdir(WEB_DIR)
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"🥕 Carrot 서버가 http://localhost:{PORT} 에서 실행 중입니다")
        print(f"종료하려면 Ctrl+C를 누르세요")
        httpd.serve_forever()
