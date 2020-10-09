import xml.etree.ElementTree as ET

tree = ET.parse('data/plants.xml')
root = tree.getroot()

print(root.tag)

for plant in root.findall('PLANT'):
    print(plant.tag, plant.find('COMMON').text)
