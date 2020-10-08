import attr


@attr.s
class Point3D(object):
    x = attr.ib()
    y = attr.ib()
    z = attr.ib()


p = Point3D(1, 2, 3)


print(p)
