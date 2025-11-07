# load_test.py
import requests
import threading
import time
import random
import sys


API_URL = "http://..."             # REST API endpoint
WEB_URL = "http://..."             # веб-сторінка
URLS = [API_URL, WEB_URL]

THREADS = 40            
REPORT_INTERVAL = 5   

stop_event = threading.Event()
counter_lock = threading.Lock()
total_requests = 0
errors = 0

def worker(id):
    global total_requests, errors
    s = requests.Session()
    while not stop_event.is_set():
        url = random.choice(URLS)
        try:
            r = s.get(url, timeout=5)
            with counter_lock:
                total_requests += 1
            if r.status_code != 200:
                with counter_lock:
                    errors += 1
        except Exception:
            with counter_lock:
                errors += 1

def reporter():
    last_total = 0
    while not stop_event.is_set():
        time.sleep(REPORT_INTERVAL)
        with counter_lock:
            t = total_requests
            e = errors
        print(f"[{time.strftime('%H:%M:%S')}] total={t} (+{t-last_total}/{REPORT_INTERVAL}s) errors={e}")
        last_total = t

if __name__ == "__main__":
    print("Starting load test. Ctrl+C to stop.")
    threads = []
    for i in range(THREADS):
        t = threading.Thread(target=worker, args=(i,), daemon=True)
        t.start()
        threads.append(t)
    rep = threading.Thread(target=reporter, daemon=True)
    rep.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping...")
        stop_event.set()
        time.sleep(1)
        with counter_lock:
            print("Final:", "total=", total_requests, "errors=", errors)
        sys.exit(0)
