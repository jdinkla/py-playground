from unittest.mock import patch
import unittest
import attr


@attr.s
class Point3D(object):
    def __init__(self, x, y, z):
        x = attr.ib
        y = attr.ib
        z = attr.ib

    def m(self):
        return self.x + self.y + self.y


def production():
    p = Point3D(1, 2, 3)
    m = p.m()
    # print("production.m=", m)
    return m


class TestStringMethods(unittest.TestCase):
    @patch('mock_test.Point3D')
    def test(self, mockclass):
        instance = mockclass.return_value
        instance.m.return_value = 1999
        result = production()
        self.assertEqual(result, 1999)
        # print("result=", result)
        instance.m.assert_called()
