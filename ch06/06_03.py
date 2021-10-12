import pybithumb
import time

con_key = "2bdd34c82dcc9aac96ead793887db3b8"
sec_key = "abe0ed795d11f363259f688582269d7c"

bithumb = pybithumb.Bithumb(con_key, sec_key)

for ticker in pybithumb.get_tickers() :
    balance = bithumb.get_balance(ticker)
    print(ticker, ":", balance)
    time.sleep(0.1)
