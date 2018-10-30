import xml.etree.ElementTree as ET

def xml_add(args):
    print get_xml_template()
    tree = ET.parse(args.path)
    print "*************"
    print tree
    root = tree.getroot()
    child = ET.ElementTree(ET.fromstring(get_xml_template()))
    root.append(child)
    tree.write(args.path)


def get_xml_template():
    node_text = ""
    node_text += "<node name=\"@node_name@\" hostname=\"@hostname@\""
    node_text += " description=\"@description@\""
    node_text += " tags=\"@tags@\" username=\"@username@\">"
    node_text += "</node>"
    return node_text
