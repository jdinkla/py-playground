
class A:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"Hi {self.name}"


class B(A):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"Moin {self.name}"


a = A("a")
b = B("b")

print(f"a says '{a.speak()}'")
print(f"b says '{b.speak()}'")
