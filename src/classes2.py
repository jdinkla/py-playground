
class A:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"Hi {self.name}"


class B:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"Moin {self.name}"

    def remain_silent(self):
        return "..."


class C(A, B):
    def __init__(self, name):
        super().__init__(name)


a = A("a")
b = B("b")
c = C("c")

print(f"a says '{a.speak()}'")
print(f"b says '{b.speak()}'")
print(f"c says '{c.speak()}'")

print(f"b says '{b.remain_silent()}'")
print(f"c says '{c.remain_silent()}'")
