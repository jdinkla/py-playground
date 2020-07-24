def flatten(ls):
    for item in ls:
        print("item", item)
        if isinstance(item, list):
            for subitem in flatten(item):
                yield subitem
        else:
            yield item

def flatten2(lol):
    for item in lol:
        print("item", item)
        if isinstance(item, list):
            yield from flatten2(item)
        else:
            yield item

lol = [1, 2, [3,4,5], [6,[7,8,9], []]]


