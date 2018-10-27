import argparse
import sys
import os

def path_state(path):
    if not os.path.exists(path):
        return "#"
    if os.path.isfile(path):
        return "f"
    else:
        return "d"

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

if not args.hostname or not args.node_name or not args.path:
    print("Hostname, Node name, and Project Path status are required, use -h for help")
    sys.exit(1)

print path_state(args.path)

# hostname = node_name = project = overwrite = None
description = tags = username = overwrite = None

if not args.description:
    description = "A Rundeck node"
if not args.tags:
    tags = "rundeck,node"
if not args.username:
    username = "root"
if not args.overwrite:
    overwrite = "false"


print description,tags,username,overwrite
# print args.overwrite


# if args.hostname:
#     hostname = args.hostname
# if args.node_name:
#     node_name = args.node_name
# if args.project:
#     project = args.project




# else:
#     print("hostname: %s, node name: %s, project name: %s" % (hostname, node_name, project))
