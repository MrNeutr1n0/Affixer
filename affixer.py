# Affixer.py
# Coded by: Abid Ahmad
# Version: 1.0

import argparse
import sys

def process_lines(input_file, output_file, prefix='', suffix=''):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                modified_line = f"{prefix}{line.strip()}{suffix}\n"
                outfile.write(modified_line)
        print(f"[INFO] - Modified lines have been saved to {output_file}")
    except Exception as e:
        print(f"[ERROR] - An error occurred: {e}")
        sys.exit(1)

def main():
    banner = r"""


 █████  ███████ ███████ ██ ██   ██ ███████ ██████  
██   ██ ██      ██      ██  ██ ██  ██      ██   ██ 
███████ █████   █████   ██   ███   █████   ██████  
██   ██ ██      ██      ██  ██ ██  ██      ██    ██ 
██   ██ ██      ██      ██ ██   ██ ███████ ██    ██ 
                                           v1.0
                                         
           Abid Ahmad  [ @MrNeutr1n0 ]
    """
    print(banner)

    parser = argparse.ArgumentParser(
        usage='affixer.py -i INPUT -o OUTPUT -b "BEFORE" -a "AFTER"',
        description='Affixer - Prefix and Suffix Adder to Each Line of a File',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('-i', '--input', required=True, help='Input file')
    parser.add_argument('-o', '--output', required=True, help='Output file to save modified lines')
    parser.add_argument('-b', '--before', default='', help='String to add before each line')
    parser.add_argument('-a', '--after', default='', help='String to add after each line')

    args = parser.parse_args()

    if not args.input or not args.output:
        parser.print_help()
        sys.exit(1)

    process_lines(args.input, args.output, args.before, args.after)

if __name__ == "__main__":
    main()
