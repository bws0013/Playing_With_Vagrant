import argparse
import sys
import os
import create_node
import add_node

def path_state(path):
    if not os.path.exists(path):
        return "#"
    if os.path.isfile(path):
        return "f"
    else:
        return "d"

def exit_with_status(status, message):
    print message
    sys.exit(status)


parser = argparse.ArgumentParser(description='Create a node')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
parser.add_argument("--hostname", "-o", help="Provide the hostname or ip of a node")
parser.add_argument("--node_name", "-n", help="Provide the name of the node (.yml will be added)")
parser.add_argument("--path", "-p", help="(optional) Provide the path of your node resource directory")
parser.add_argument("--description", "-d", help="(optional) Provide a node description")
parser.add_argument("--tags", "-t", help="(optional) Provide a comma separated list of tags (enter no spaces in the tag list)")
parser.add_argument("--username", "-u", help="(optional) Provide a user to login as (default is root)")
parser.add_argument("--overwrite", "-v", help="(true/false) Overwrite existing node with same name (default: false)")

args = parser.parse_args()

# if not args.hostname or not args.node_name or not args.path:
#     exit_with_status(1, "Hostname, Node name, and Project Path status are required, use -h for help")

file_type = path_state(args.path)
if file_type == "#":
    exit_with_status(2, "File either doesn't exist or isn't in a readable location.")
elif file_type == "d":
    create_node.create_node_file_from_args(args)
elif file_type == "f":
    add_node.world()

# if args.hostname:
#     hostname = args.hostname
# if args.node_name:
#     node_name = args.node_name
# if args.project:
#     project = args.project




# else:
#     print("hostname: %s, node name: %s, project name: %s" % (hostname, node_name, project))
