import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    pom = 0
    for elem in node.iter():
        if elem.attrib:
            pom = pom + len(elem.attrib)
    return pom

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))