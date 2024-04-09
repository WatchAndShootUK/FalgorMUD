import threading
import time
from engine.heartbeat import heartbeat


class Heartbeat:
    def __init__(self):
        self.timer = None
        self.is_running = False

    def _run(self):
        while self.is_running:
            heartbeat()
            time.sleep(1.5)

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.timer = threading.Thread(target=self._run)
            self.timer.start()

    def stop(self):
        if self.is_running:
            self.is_running = False
            self.timer.join()