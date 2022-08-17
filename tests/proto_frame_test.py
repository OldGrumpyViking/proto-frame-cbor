import importlib.metadata

import proto_frame.cbor as pf_cbor


def test_version():
    """Tests that the different ways of getting the version of the package is working."""
    assert importlib.metadata.version("proto_frame_cbor") == pf_cbor.__version__
