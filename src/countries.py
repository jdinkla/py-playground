import xml.etree.ElementTree as ET

tree1 = ET.parse('data/countries.xml')
tree2 = ET.parse('data/countries_diff.xml')


def get_nodes_sorted(tree, tag, keyf):
    root = tree.getroot()
    countries = root.findall(tag)
    countries.sort(key=keyf)
    return countries


def key_fun(elem): return elem.attrib['name']


countries1 = get_nodes_sorted(tree1, 'country', key_fun)
countries2 = get_nodes_sorted(tree2, 'country', key_fun)

print([c.get('name') for c in countries1])
print([c.get('name') for c in countries2])


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


walk(countries1,
     countries2,
     key_fun,
     lambda v: print("LEFT " + key_fun(v)),
     lambda v, w: print("EQ " + key_fun(v) + " " + key_fun(w)),
     lambda v: print("RIGHT " + key_fun(v))
     )
