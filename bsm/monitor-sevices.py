import time
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


monitor_dir = "/home/hayder/bsm/test"
log_file = "/home/hayder/bsm/logs/changes.json"


class ChangeHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        log_entry = {
            "event_type": event.event_type,
            "path": event.src_path,
            "is_directory": event.is_directory,
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
        }
        print(f"Detected change: {log_entry}")
        with open(log_file, "a") as f:
            f.write(json.dumps(log_entry) + "\n")

if __name__ == "__main__":
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, monitor_dir, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

