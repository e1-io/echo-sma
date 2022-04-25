from echo1_sma.echo1_sma import StreamingMovingAverage


def test_version():

    sma = StreamingMovingAverage(2)
    sma.append_value(1)
    sma.append_value(2)
    assert sma.append_value(3) == 2.5
    assert sma.get_sma() == 2.5
