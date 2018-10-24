import argparse

parser = argparse.ArgumentParser(description='Create a node')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

args = parser.parse_args()
print(args.accumulate(args.integers))
