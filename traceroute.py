import subprocess
from utils import validate_ip_range

def clean_output(raw_output):
    """Clean and format the raw traceroute output into a user-friendly format."""
    lines = raw_output.splitlines()
    output = []
    output.append(f"{'Hop':<5} {'IP Address':<20} {'Hostname':<30} {'Response Time':<15}")

    for line in lines:
        # Match lines containing traceroute hop details
        if line.startswith("  "):
            parts = line.split()
            hop = parts[0].strip()  # Hop number
            ip_address = parts[1].strip("()")  # IP Address
            hostname = parts[2] if len(parts) > 2 else "N/A"  # Hostname if available
            response_time = parts[-1] if len(parts) > 3 else "N/A"  # Response time
            output.append(f"{hop:<5} {ip_address:<20} {hostname:<30} {response_time:<15}")

    return "\n".join(output)

def traceroute():
    """Perform a traceroute scan to track the network path."""
    target = input("Enter the target IP or name (e.g., google.com): ")

    # Use the new validation function that handles both IPs and domain names
    while not validate_ip_range(target):
        print("Invalid IP or name format! Please use the correct format (e.g., google.com).")
        target = input("Enter the target IP or name (e.g., google.com): ")

    command = f"nmap --traceroute {target}"
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

