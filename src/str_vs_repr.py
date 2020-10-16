
class A():
    def __str__(self):
        return "A.STR"


class B(A):
    def __repr__(self):
        return "B.REPR"


a = A()
b = B()
print([a, b])
print(str([a, b]))
print(*map(str, [a, b]))
