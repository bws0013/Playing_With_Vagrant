import xml.etree.ElementTree as ET

def xml_add(args):

    root = ET.parse(args.path).getroot()
    child = ET.ElementTree(ET.fromstring(get_xml_template()))
    root.append(child)
    tree.write(args.path)


def get_xml_template():
    node_text = """
    <node name=\"@node_name@\" hostname=\"@hostname@\""
      description=\"@description@\""
      tags=\"@tags@\" username=\"@username@\">"
    </node>"
    """
    return node_text
