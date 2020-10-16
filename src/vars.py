class A:
    x = 13

    def __init__(self, y):
        self.y = y

    def __str__(self):
        return f"x={x},y={self.y}"


a = A(1)
b = A(2)
print(f"{a.x} {b.x}")

A.x = 14
print(f"{a.x} {b.x}")

b.x = 15
print(f"{a.x} {b.x}")
