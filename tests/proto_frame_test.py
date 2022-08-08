import importlib.metadata

import proto_frame


def test_version():
    assert importlib.metadata.version("proto_frame") is not None
    assert proto_frame.__version__ is not None

    assert importlib.metadata.version("proto_frame") == proto_frame.__version__
