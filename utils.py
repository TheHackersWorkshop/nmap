import os
import re
import socket
import ipaddress

def validate_ip_range(ip_range):
    """Validate if the input is a valid IP address, IP range, or domain name."""

    # Check if it's an IP range (e.g., 192.168.1.1-100 or 10.0.0.10-20)
    pattern = r"^(\d{1,3}\.){3}\d{1,3}(-\d{1,3})?$"

    # First, check if it's a valid IP range
    if re.match(pattern, target):
        base_ip, *end_ip = target.split('-')

        # Validate base IP
        try:
            ipaddress.ip_address(base_ip)
        except ValueError:
            return False

        # If there is a range (e.g., 192.168.1.1-100), validate the range part
        if end_ip:
            try:
                end_ip = int(end_ip[0])
                if not (0 <= end_ip <= 255):  # Ensure the range is between 0-255
                    return False
            except ValueError:
                return False

        return True

    # Second, check if it's an individual IP address (e.g., 192.168.1.1)
    try:
        ipaddress.ip_address(target)
        return True
    except ValueError:
        pass  # If it's not a valid IP, we move on to domain validation

    # Finally, check if it's a valid domain name (e.g., google.com)
    try:
        socket.gethostbyname(target)  # Try resolving the domain name
        return True
    except socket.error:
        return False  # It's neither a valid IP nor domain name

def clean_output(output):
    """
    Clean and prettify the Nmap output (basic text processing).
    Strips extra whitespace or lines, leaving readable output.
    """
    return output.strip()


def get_local_network():
    """
    Get the local network range in CIDR notation (e.g., 192.168.1.0/24).
    This assumes a /24 subnet mask as default for simplicity.
    """
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    network = ipaddress.ip_network(local_ip + "/24", strict=False)
    return str(network)


def format_table(data, headers):
    """
    Create a simple ASCII table using headers and rows of data.
    Example:
        headers = ["IP", "Status"]
        data = [["192.168.1.1", "Up"], ["192.168.1.2", "Down"]]

    Returns:
        A formatted string representation of the table.
    """
    # Determine column widths based on the headers and data
    col_widths = [len(header) for header in headers]
    for row in data:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    # Build header row
    header_row = " | ".join(f"{header:<{col_widths[i]}}" for i, header in enumerate(headers))
    separator = "-+-".join("-" * col_width for col_width in col_widths)

    # Build data rows
    rows = []
    for row in data:
        rows.append(" | ".join(f"{cell:<{col_widths[i]}}" for i, cell in enumerate(row)))

    # Combine all rows into a single table string
    return f"{header_row}\n{separator}\n" + "\n".join(rows)

import ipaddress

def convert_ip_range(ip_range):
    """
    Convert an IP range (e.g., 192.168.1.1-100) to a list of individual IP addresses.
    Assumes the input is in the form 'start_ip-end_ip' or 'single_ip'.
    """
    # Check if the input is a range (e.g., 192.168.1.1-100)
    if '-' in ip_range:
        base_ip, end_ip = ip_range.split('-')
        base_ip_parts = base_ip.split('.')
        start_ip = int(base_ip_parts[-1])
        end_ip = int(end_ip)

        # Generate IP range
        ips = []
        for i in range(start_ip, end_ip + 1):
            ips.append(".".join(base_ip_parts[:-1] + [str(i)]))
        return " ".join(ips)

    # If it's not a range, return the single IP
    return ip_range

def check_sudo():
    """Ensure the script is run with sudo privileges"""
    if os.geteuid() != 0:
        print("This script requires sudo. Please run as root.")
        exit(1)

