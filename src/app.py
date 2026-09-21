import os
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread

import psycopg


def get_message():
    return "DevOps app is running"


def check_database():
    with psycopg.connect(
        host=os.getenv("DB_HOST", "db"),
        port=int(os.getenv("DB_PORT", "5432")),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1")
            return cursor.fetchone()[0] == 1


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/health":
            self.send_response(404)
            self.end_headers()
            return

        try:
            healthy = check_database()

            if healthy:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'{"status":"ok"}')
            else:
                self.send_response(503)
                self.end_headers()
        except Exception:
            self.send_response(503)
            self.end_headers()

    def log_message(self, format, *args):
        return


def start_http_server():
    server = ThreadingHTTPServer(("0.0.0.0", 8080), HealthHandler)
    server.serve_forever()


def run():
    http_thread = Thread(target=start_http_server, daemon=True)
    http_thread.start()

    while True:
        print(get_message(), flush=True)
        time.sleep(5)


if __name__ == "__main__":
    run()
