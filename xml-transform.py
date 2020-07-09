import xml.etree.ElementTree as ET

tree = ET.parse('data/regression.xml')
root = tree.getroot()

for comp in root.find('Components').findall('Component'):
    print(comp.get('name'))

    for vcar in comp.findall('Modules/Module/Tests/VCars/VCar'):
        print("  " + str(vcar.get('file')))
