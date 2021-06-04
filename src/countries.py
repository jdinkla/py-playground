import xml.etree.ElementTree as ET
from xml_diff import get_nodes_sorted, walk, elements_equal, elements_equal2
from xml.etree.ElementTree import XMLParser


parser = XMLParser()
tree1 = ET.parse('data/countries.xml', parser)

parser = XMLParser()
tree2 = ET.parse('data/countries_diff.xml', parser)


def key_fun(elem): return elem.attrib['name']


countries1 = get_nodes_sorted(tree1, 'country', key_fun)
countries2 = get_nodes_sorted(tree2, 'country', key_fun)

print([c.get('name') for c in countries1])
print([c.get('name') for c in countries2])

walk(countries1,
     countries2,
     key_fun,
     lambda v: print("LEFT " + key_fun(v)),
     lambda v, w: print("EQ " + key_fun(v) + " == " +
                        key_fun(w) + " = " + str(elements_equal2(v, w))),
     lambda v: print("RIGHT " + key_fun(v))
     )


def xml_diff(lhs, rhs, key_fun):

    walk(lhs,
         rhs,
         key_fun,
         lambda v: print("LEFT " + key_fun(v)),
         lambda v, w: print("EQ " + key_fun(v) + " == " +
                            key_fun(w) + " = " + str(elements_equal(v, w))),
         lambda v: print("RIGHT " + key_fun(v))
         )


xml_diff(countries1, countries2, key_fun)
