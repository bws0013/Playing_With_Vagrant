import argparse

parser = argparse.ArgumentParser(description='Create a node')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
parser.add_argument("--hostname", "-H", help="Provide the hostname or ip of a node")
parser.add_argument("--node_name", "-n", help="Provide the name of the node (.yml will be added)")
parser.add_argument("--project", "-p", help="Provide the hostname or ip of a node")

args = parser.parse_args()

hostname = node_name = project = None

if args.hostname:
    hostname = args.hostname
if args.node_name:
    node_name = args.node_name
if args.project:
    project = args.project

if not args.hostname or not args.node_name or not args.project:
    print("Hostname, Node name and Project name are required, use -h for help")
else:
    print("hostname: %s, node name: %s, project name: %s" % (hostname, node_name, project))
