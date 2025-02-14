import pybithumb
import numpy as np

df = pybithumb.get_ohlcv("BTC")
df = df['2020']
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)

fee = 0.0032
# fee = 0.00032
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] - fee,
                     1)

ror = df['ror'].cumprod()[-2]
print(ror)

