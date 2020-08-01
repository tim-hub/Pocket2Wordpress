import argparse
from src.worker.main import main, OutputMode

parser = argparse.ArgumentParser(description='Output mode, WP wordpress or MD markdown.')
parser.add_argument('mode', metavar='OutputMode', type=str, default=OutputMode.WP,
                    help='The output mode, MD/WP')

args = parser.parse_args()

print('mode ' + args.mode)
main(args.mode)
