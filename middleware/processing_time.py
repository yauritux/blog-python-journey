import time

def processing_time(fn):

    def wrapper(*args, **kwargs):
        start = time.process_time()
        print("starting at", start)
        print(fn(*args, **kwargs))
        end = time.process_time()
        print("finished at", end)
        print("process took", "{:.8f}".format(float(end - start)), "s")

    return wrapper
