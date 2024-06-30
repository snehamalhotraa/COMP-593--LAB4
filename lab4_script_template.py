import sys
import re
import pandas as pd

def main():
    log_file = get_log_file_path_from_cmd_line()

    records, _ = filter_log_by_regex(log_file, r'sshd', ignore_case=True, print_summary=True, print_records=True)
    port_traffic = tally_port_traffic(log_file)
    generate_port_traffic_report(log_file, 22)  
    generate_invalid_user_report(log_file)
    generate_source_ip_log(log_file, '220.195.35.40')

# TODO: Step 3
def get_log_file_path_from_cmd_line(param_number):
    if len(sys.argv) <= param_number:
        print(f"[Error] Command line parameter #{param_number} is missing.")
        sys.exit(1)
    log_file_path = sys.argv[param_number]
    try:
        with open(log_file_path, 'r') as file:
            pass
    except FileNotFoundError:
        print(f"[Error] The specified file does not exist: {log_file_path}")
        sys.exit(1)

    return log_file_path


# TODO: Steps 4-7
def filter_log_by_regex(log_file, regex, ignore_case=True, print_summary=False, print_records=False):
    flags = re.IGNORECASE if ignore_case else 0
    pattern = re.compile(regex, flags)
    matching_records = []
    captured_data = []

    with open(log_file, 'r') as file:
        for line in file:
            match = pattern.search(line)
            if match:
                matching_records.append(line.strip())
                captured_data.append(match.groups())

    if print_records:
        for record in matching_records:
            print(f"[Record] {record}")
    if print_summary:
        print(f"[Summary] The log file contains {len(matching_records)} records that {'case-insensitive ' if ignore_case else ''}match the regex \"{regex}\".")
     
    return matching_records, captured_data

# TODO: Step 8
def tally_port_traffic(log_file):
    return

# TODO: Step 9
def generate_port_traffic_report(log_file, port_number):
    return

# TODO: Step 11
def generate_invalid_user_report(log_file):
    return

# TODO: Step 12
def generate_source_ip_log(log_file, ip_address):
    return

if __name__ == '__main__':
    main()