#!/usr/bin/python3

import sys

def print_metrics(total_size, status_codes):
    """Prints the metrics."""
    print("File size: {}".format(total_size))
    for status_code in sorted(status_codes.keys()):
        print("{}: {}".format(status_code, status_codes[status_code]))

def parse_line(line, total_size, status_codes):
    """Parses a line and updates the metrics."""
    parts = line.split()
    if len(parts) >= 2:
        total_size += int(parts[-1])
        status_code = parts[-2]
        if status_code in status_codes:
            status_codes[status_code] += 1
        else:
            status_codes[status_code] = 1
    return total_size, status_codes

def main():
    """Main function."""
    total_size = 0
    status_codes = {}
    line_count = 0

    try:
        for line in sys.stdin:
            total_size, status_codes = parse_line(line, total_size, status_codes)
            line_count += 1
            if line_count % 10 == 0:
                print_metrics(total_size, status_codes)
    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()
