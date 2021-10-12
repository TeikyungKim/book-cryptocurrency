import pybithumb
import time

while True:
    price = pybithumb.get_current_price("BTC")
    if price is not None:
        print(price / 10)
    time.sleep(0.2)