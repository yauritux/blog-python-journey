from datetime import datetime
import time


class Logger:

    def __init__(self, fn):
        self._fn = fn

    def __call__(self, *args, **kwargs):
        start = time.process_time()
        file = open("log.txt", "a+")
        result = self._fn(*args, **kwargs)
        output = f"{datetime.now()} - {self._fn.__name__} is executed. Time taken: {float(time.process_time() - start)} s\n"
        file.write(output)
        file.close()
        return result
