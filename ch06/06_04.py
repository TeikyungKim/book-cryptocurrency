import pybithumb

con_key = "2bdd34c82dcc9aac96ead793887db3b8"
sec_key = "abe0ed795d11f363259f688582269d7c"

bithumb = pybithumb.Bithumb(con_key, sec_key)

order = bithumb.buy_limit_order("BTC", 390000, 0.0001)
print(order)
