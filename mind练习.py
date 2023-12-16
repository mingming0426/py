
import datetime
import time



while True:
    time.sleep(1)
    print(datetime.datetime.now().year,end="")
    print(" ",end="")
    print(time.strftime("%H:%M:%S"))
