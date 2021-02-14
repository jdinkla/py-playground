
def gen(n):
    a = ""
    for _ in range(0, n):
        print("Before ", a)
        yield a
        print("After ", a)
        a += "|"


g4 = gen(4)
print(*g4)


def gen2(n):
    return ("|" * i for i in range(0, n))


g24 = gen2(4)
print(g24)
