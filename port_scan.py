import subprocess
from utils import validate_ip_range, convert_ip_range

def clean_output(raw_output):
    """Clean and format the raw Nmap output into a user-friendly format."""
    lines = raw_output.splitlines()
    output = []
    output.append(f"{'Host':<30} {'Port':<10} {'State':<10} {'Service':<20}")
    host = None

    for line in lines:
        if "Nmap scan report for" in line:
            host = line.split()[-1]
        elif "/tcp" in line or "/udp" in line:
            parts = line.split()
            port = parts[0]  # e.g., "22/tcp"
            state = parts[1]  # e.g., "open"
            service = " ".join(parts[2:])  # Remaining part as service name
            output.append(f"{host:<30} {port:<10} {state:<10} {service:<20}")

    return "\n".join(output)

def validate_port_range(port_range):
    """Validate the port range format (e.g., 22-80 or 22,80,443)."""
    import re
    pattern = re.compile(r"^\d+(-\d+)?(,\d+(-\d+)?)*$")
    return bool(pattern.match(port_range))

def port_scan():
    """Perform port scanning with a custom port range and target IP."""
    target = input("Enter the target IP range (e.g., 192.168.50.20-253): ")
    while not validate_ip_range(target):
        print("Invalid IP range format! Please use the correct format (e.g., 192.168.50.20-253).")
        target = input("Enter the target IP range (e.g., 192.168.50.20-253): ")

    target_full_range = convert_ip_range(target)  # Convert to full IP range
    port_range = input("Enter the port range (e.g., 22-80 or 22,80,443): ")
    while not validate_port_range(port_range):
        print("Invalid port range format! Please use the correct format.")
        port_range = input("Enter the port range (e.g., 22-80 or 22,80,443): ")

    command = f"nmap -p {port_range} {target_full_range}"
    print(f"Running command: {command}")
    run_nmap(command)

def run_nmap(command):
    """Run nmap command silently and clean the output."""
    try:
        # Run Nmap and suppress output to the terminal
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        output = result.decode()

        # Clean the output and show only the relevant information
        cleaned_output = clean_output(output)
        print("\nScan Results:\n")
        print(cleaned_output)

    except subprocess.CalledProcessError as e:
        print(f"Error running nmap command: {e}")
