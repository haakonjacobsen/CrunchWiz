import backend.preprocessing.dummy_producer as dp


class TestPrpducer:
    def test_producer(self):
        x = dp.DummyProducer()
        assert (x.f() == "hei")

    def test_DummyProducerThatStoresTheStream(self):
        x = dp.DummyProducerThatStoresTheStream()
        assert (x.f() == "hello world")
