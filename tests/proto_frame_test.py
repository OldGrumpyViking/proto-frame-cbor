import importlib.metadata

import proto_frame.core as pf_core


def test_version():
    """Tests that the different ways of getting the version of the package is working."""
    assert importlib.metadata.version("proto_frame") == pf_core.__version__
