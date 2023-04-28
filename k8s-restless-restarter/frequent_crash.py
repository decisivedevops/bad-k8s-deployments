import os
import random
import time
import sys

sleep_time_range = int(os.getenv("SLEEP_TIME_RANGE", 5))

LOG_LINES = [
    "INFO: App started successfully.",
    "WARNING: Connection timeout.",
    "WARNING: Service rate limit reached.",
    "INFO: Data processed successfully.",
    "DEBUG: Intermediate step completed.",
    "INFO: User authentication successful.",
    "WARNING: API call took longer than expected.",
    "DEBUG: Data parsing completed.",
    "INFO: Request sent to the external service.",
    "DEBUG: Successfully updated cache.",
    "ERROR: Failed to fetch data from the database."
]


def simulate_real_world_app(sleep_time_range):
    while True:
        log_line = random.choice(LOG_LINES)
        print(log_line)
        sleep_time = random.randint(1, sleep_time_range)
        time.sleep(sleep_time)
        if "ERROR" in log_line:
            sys.exit(1)


if __name__ == '__main__':
    simulate_real_world_app(sleep_time_range)
