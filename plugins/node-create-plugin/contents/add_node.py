import xml.etree.ElementTree as ET

def xml_add(args):
    node_text = get_xml_template()
    node_text = node_text.replace("@node_name@", args.node_name)
    node_text = node_text.replace("@description@", args.description)
    node_text = node_text.replace("@hostname@", args.hostname)
    node_text = node_text.replace("@username@", args.username)
    node_text = node_text.replace("@tags@", args.tags)

    import xml.etree.ElementTree as ET
    tree = ET.parse('output/resources.xml')
    root = tree.getroot()
    for child in root.findall('node'):
        print child.get('name')



def get_xml_template():
    node_text = "  "
    node_text += "<node name=\"@node_name@\" hostname=\"@hostname@\""
    node_text += " description=\"@description@\""
    node_text += " tags=\"@tags@\" username=\"@username@\"></node>"
    return node_text
