import time
import os

memory_increment_mb = int(os.environ.get("MEMORY_INCREMENT_MB", 1))
sleep_time = int(os.environ.get("SLEEP_TIME", 1))


def consume_memory():
    memory_hog = []
    try:
        while True:
            # Consume MEMORY_INCREMENT_MB MB of memory
            memory_hog.append(os.urandom(memory_increment_mb * 1024 * 1024))
            time.sleep(sleep_time)  # Wait for 1 second
    except MemoryError:
        print("Memory limit reached. Exiting.")


if __name__ == "__main__":
    consume_memory()
