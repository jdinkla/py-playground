from collections import namedtuple
from typing import NamedTuple


Point3D = namedtuple('Point3D', ('x', 'y', 'z'))

p = Point3D(1, 2, 3)

s = p.x + p.y + p.z

x, y, z = p

print(p._asdict())


class P3D(NamedTuple):
    x: float
    y: float
    z: float

    def plus(self, other):
        return P3D(self.x + other.x, self.y + other.y, self.z + other.z)


q = P3D(1, 2, 3)

print(q, q.plus(q))

