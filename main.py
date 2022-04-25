from echo1_sma.echo1_sma import StreamingMovingAverage

sma = StreamingMovingAverage(2)
sma.append_value(1)
sma.append_value(2)
print(sma.append_value(3))
