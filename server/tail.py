import os
import time
def tail(_1,filename,_iter):
    with open(filename) as f:
        f.seek(0, os.SEEK_END)
        while True:
            # read last line of file
            line = f.readline()
            # sleep if file hasn't been updated
            if not line:
                time.sleep(0.05)
                continue
            yield line