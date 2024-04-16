import os
from dotenv import load_dotenv, dotenv_values 
from http.server import HTTPServer, BaseHTTPRequestHandler
import time 
load_dotenv() 

HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))
class NeuralHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>Welcome to the HTTP Server!</h1></body></html>","utf-8"))
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes('"time": "{}"'.format(date), "utf-8"))
try:
    server = HTTPServer((HOST, PORT), NeuralHTTP)
    print(f"Server running at http://{HOST}:{PORT}")
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped")
    server.server_close()  