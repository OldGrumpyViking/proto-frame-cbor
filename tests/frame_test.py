import proto_frame.cbor as pf_core_cbor


class TestFrame:
    def test_bytes(self):
        res = bytes(range(10))
        tst_frame = pf_core_cbor.CborFrame.from_bytes(res)
        assert tst_frame.to_bytes() == res
