#!/usr/bin/env python3
"""
script that reads stdin line by line and computes metrics
"""
import re
import sys
import signal
import threading
possible_status = {200, 301, 400, 401, 403, 404, 405, 500}
count = 0
status_count = {}
files_size = 0
pattern = re.compile(
    r'('
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'  # IP Address
    r') - \['
    r'(.*?)'  # Date
    r'\] "GET /projects/260 HTTP/1\.1" '
    r'(\d{3})'  # Status Code
    r' (\d+)'  # File Size
)
# Create a lock object
lock = threading.Lock()


# Define signal handler
def handle_signal(sig, frame):
    with lock:
        # Buffer the output
        output = [f'File size: {files_size}']
        output.extend(f'{status}: {status_num}' for status,
                      status_num in sorted(status_count.items()))
        sys.stdout.write("\n".join(output) + "\n")
        sys.stdout.flush()
    sys.exit(0)  # Exit the program cleanly


signal.signal(signal.SIGINT, handle_signal)


def main():
    global count, files_size, status_count

    for line in sys.stdin:
        if not pattern.match(line):
            continue

        line_split = line.split()
        status = int(line_split[-2])
        file_size = int(line_split[-1])

        if status in possible_status:
            if status in status_count:
                status_count[status] += 1
            else:
                status_count[status] = 1

        files_size += file_size
        count += 1

        if count % 10 == 0:
            # Buffer output to avoid interleaving
            output = [f'File size: {files_size}']
            output.extend(f'{status}: {status_num}' for status,
                          status_num in sorted(status_count.items()))
            sys.stdout.write("\n".join(output) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
