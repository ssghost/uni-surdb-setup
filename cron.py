import schedule
import time
from upload import *

if __name__ == '__main__':
    schedule.every().week.do(upload)

    while True:
        schedule.run_pending()
        time.sleep(1)