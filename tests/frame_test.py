from proto_frame.core import frame


class TestFrame:
    def test_bytes(self):
        res = bytes(range(10))
        tst_frame = frame.Frame.from_bytes(res)
        assert tst_frame.to_bytes() == res
