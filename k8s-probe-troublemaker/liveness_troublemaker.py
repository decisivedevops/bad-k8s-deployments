import os
import random
import time
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

LOG_LINES = [
    "INFO: App started successfully.",
    "WARNING: Connection timeout.",
    "INFO: Data processed successfully.",
    "DEBUG: Intermediate step completed.",
    "INFO: User authentication successful.",
    "WARNING: API call took longer than expected.",
    "DEBUG: Data parsing completed.",
    "INFO: Request sent to the external service.",
    "DEBUG: Successfully updated cache."
]


failed_checks = 0


class ProbeTroubleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global failed_checks
        if self.path == '/readiness':
            self.send_response(200)
            self.end_headers()
        elif self.path == '/liveness':
            if failed_checks < 10:
                self.send_response(200)
                failed_checks += 1
            else:
                self.send_response(503)
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()


def simulate_real_world_app(log_sleep_time_range):
    while True:
        log_line = random.choice(LOG_LINES)
        print(log_line)
        sleep_time = random.randint(1, log_sleep_time_range)
        time.sleep(sleep_time)


if __name__ == '__main__':
    log_sleep_time_range = int(os.getenv("LOG_SLEEP_TIME_RANGE", 10))
    server_port = int(os.getenv("SERVER_PORT", 8080))

    server = HTTPServer(('0.0.0.0', server_port), ProbeTroubleHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    simulate_real_world_app(log_sleep_time_range)
