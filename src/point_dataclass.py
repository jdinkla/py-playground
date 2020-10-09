from dataclasses import dataclass


@dataclass
class Point3d(object):
    x: float
    y: float
    z: float

    def sqr_distance(self):
        return self.x*self.x + self.y*self.y + self.z*self.z


p = Point3d(1, -2, 3)

print(p)
print(p.sqr_distance())
