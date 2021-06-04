import pprint
from xmldiff import main


file1 = 'data/countries.xml'
file2 = 'data/countries_diff2.xml'

pp = pprint.PrettyPrinter(indent=2)

diff = main.diff_files(file1, file2, {'ratio_mode': 'accurate', 'F': 0.1, 'uniqueattrs': ["name"]})
pp.pprint(diff)

patch = main.patch_file(file1, file2)
pp.pprint(patch)
