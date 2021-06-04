

def get_nodes_sorted(tree, tag, key_fun):
    root = tree.getroot()
    nodes = root.findall(tag)
    nodes.sort(key=key_fun)
    return nodes


def walk(lhs, rhs, key_fun, left_fun, eq_fun, right_fun):
    left_i = 0
    right_i = 0
    while left_i < len(lhs) or right_i < len(rhs):
        if left_i == len(lhs):
            val2 = rhs[right_i]
            key2 = key_fun(val2)
            key1 = "[larger than Z"
        else:
            val1 = lhs[left_i]
            val2 = rhs[right_i]
            key1 = key_fun(val1)
            key2 = key_fun(val2)
        if key1 == key2:
            eq_fun(val1, val2)
            left_i += 1
            right_i += 1
        elif key1 < key2:
            left_fun(val1)
            left_i += 1
        else:
            right_fun(val2)
            right_i += 1


# from https://stackoverflow.com/questions/7905380/testing-equivalence-of-xml-etree-elementtree
def elements_equal(e1, e2):
    if e1.tag != e2.tag:
        return False
    if e1.text != e2.text:
        return False
#    if e1.tail != e2.tail:
#        return False
    if e1.attrib != e2.attrib:
        return False
    if len(e1) != len(e2):
        return False
    return all(elements_equal(c1, c2) for c1, c2 in zip(e1, e2))


flatten = lambda t: [item for sublist in t for item in sublist]  # noqa: E731


# modified, from https://stackoverflow.com/questions/7905380/testing-equivalence-of-xml-etree-elementtree
def elements_equal2(e1, e2):
    if e1.tag != e2.tag:
        return ("tag", e1.tag, e2.tag)
    if e1.text != e2.text:
        return ("text", e1.text, e2.text)
#    if e1.tail != e2.tail:
#        return ("tail", e1.tail, e2.tail)
    if e1.attrib != e2.attrib:
        return ("attrib", e1.attrib, e2.attrib)
    if len(e1) != len(e2):
        return ("len", e1, e2)
    return flatten([elements_equal2(c1, c2) for c1, c2 in zip(e1, e2)])
