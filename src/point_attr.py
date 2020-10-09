import attr


@attr.s
class Point3D(object):
    x = attr.ib()
    y = attr.ib()
    z = attr.ib()

    def sqr_distance(self):
        return self.x*self.x + self.y*self.y + self.z*self.z


p = Point3D(1, 2, 3)

print(p)
print(p.sqr_distance())
