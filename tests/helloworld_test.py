from proto_frame import helloworld


def test_hello():
    assert helloworld.hello() == "World"
