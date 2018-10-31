import sys
import xml.etree.ElementTree as ET

def exit_with_status(status, message):
    print message
    sys.exit(status)

def xml_add(args):
    node_text = get_xml_template()
    node_text = node_text.replace("@node_name@", args.node_name)
    node_text = node_text.replace("@description@", args.description)
    node_text = node_text.replace("@hostname@", args.hostname)
    node_text = node_text.replace("@username@", args.username)
    node_text = node_text.replace("@tags@", args.tags)
    node_element = ET.fromstring(node_text)

    tree = ET.parse(args.path)
    root = tree.getroot()
    for child in root.findall("node"):
        if child.get("name") == args.node_name and args.overwrite == "false":
            exit_with_status(6, "The node you are adding already exists and overwrite is set to false.")
        elif child.get("name") == args.node_name and args.overwrite == "true":
            root.remove(child)
            break
    tree.write(args.path)

    # TODO add feature for writing new node to the file
    # perhaps it should be another method


def get_xml_template():
    node_text = "  "
    node_text += "<node name=\"@node_name@\" hostname=\"@hostname@\""
    node_text += " description=\"@description@\""
    node_text += " tags=\"@tags@\" username=\"@username@\"></node>"
    return node_text
