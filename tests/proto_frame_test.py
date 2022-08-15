import importlib.metadata

import proto_frame


def test_version():
    """Tests that the different ways of getting the version of the package is working."""
    assert importlib.metadata.version("proto_frame") is not None
    assert importlib.metadata.version("proto_frame") == proto_frame.__version__
