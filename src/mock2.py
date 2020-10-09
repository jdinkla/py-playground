from unittest.mock import patch
import attr


@attr.s
class Point3D(object):
    x = attr.ib()
    y = attr.ib()
    z = attr.ib()

    def m(self):
        return self.x + self.y + self.y


def test():
    p = Point3D(1, 2, 3)
    m = p.m()
    print("test.m=", m)
    return m


def mocked():
    print("start")
    with patch('mock.Point3D') as mock:
        instance = mock.return_value
        instance.m.return_value = 99
        result = test()
        print("result=", result)
    print("exit")


def __main__():
    # print("test=", test())
    print("XX start")
    mocked()
    print("XX exit")


__main__()