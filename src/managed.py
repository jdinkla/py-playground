

class Managed():

    def __init__(self):
        print("     __init__")
        self.managed = None

    def __enter__(self):
        print("     __enter__")
        self.managed = "Some"
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("     __exit__")
        if self.managed:
            self.managed = None

    def do_sth(self):
        print("     do_sth: " + self.managed)


print("start")
with Managed() as m:
    print("before")
    m.do_sth()
    print("after")

print("end")
