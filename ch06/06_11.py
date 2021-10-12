import pybithumb
import time

con_key = "2bdd34c82dcc9aac96ead793887db3b8"
sec_key = "abe0ed795d11f363259f688582269d7c"

bithumb = pybithumb.Bithumb(con_key, sec_key)

order = bithumb.buy_limit_order("BTC", 3000000, 0.001 )
print(order)

time.sleep(10)
cancel = bithumb.cancel_order(order)
print(cancel)
