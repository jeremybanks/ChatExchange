import pprintpp



def update(o: object, **attrs):
    for name, value in attrs.items():
        assert hasattr(o, name)
        setattr(o, name, value)


def repr(o: object):
    return type(o).__qualname__ + pprintpp.pformat(o.__dict__)
