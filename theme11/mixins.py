import json


class LogMixin:
    def log(self, message):
        print(f"[LOG] {message}")


class JsonMixin:
    def to_json(self):
        return json.dumps(self.__dict__)
