
def f(** args):
    print("args:", *args)
    if "a" in args:
        print("a is ", args["a"])
    else:
        print("No a")


f(a="c", b="b")


f(c="c")
