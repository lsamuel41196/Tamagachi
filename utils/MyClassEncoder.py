import json
import threading

class MyClassEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, threading.Thread):
            return None  # or any other representation of your thread objects, e.g., "Thread"
        return super().default(obj)