#!/usr/bin/python3
"""Parsing HTTP request logs.
"""
import re


def get_input(input_line):
    """Extracts the IP, date, request, status code, and file size
    """
    proj = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(
        proj[0], proj[1], proj[2], proj[3], proj[4])
    response = re.fullmatch(log_fmt, input_line)
    if response is not None:
        status_code = response.group('status_code')
        file_size = int(response.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info


def print_stats(total_file_size, status_codes_stats):
    """Prints the statistics of the parsed HTTP request logs.
    """
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    """Updates the metrics of the parsed HTTP request logs.
    """
    line_info = get_input(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_codes_stats.keys():
        status_codes_stats[status_code] += 1
    return total_file_size + line_info['file_size']


if __name__ == '__main__':
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            total_file_size = update_metrics(
                line,
                total_file_size,
                status_codes_stats,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_stats(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_stats(total_file_size, status_codes_stats)
