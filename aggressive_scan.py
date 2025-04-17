import subprocess
from utils import validate_ip_range, convert_ip_range, format_table

def aggressive_scan():
    """Perform an aggressive scan to gather detailed info."""
    target = input("Enter the target IP range (e.g., 192.168.50.20-253): ")
    while not validate_ip_range(target):
        print("Invalid IP range format! Please use the correct format (e.g., 192.168.50.20-253).")
        target = input("Enter the target IP range (e.g., 192.168.50.20-253): ")

    target_full_range = convert_ip_range(target)  # Convert to full IP range
    command = f"nmap -A {target_full_range}"
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


def clean_output(raw_output):
    """Clean and format the raw Nmap output into a user-friendly format."""
    lines = raw_output.splitlines()
    headers = ["Host", "OS Details", "Ports", "Services"]
    data = []

    # Variables to store parsed data
    host = None
    os_details = "Unknown"
    ports = []
    services = []

    for line in lines:
        if "Nmap scan report for" in line:
            # If there's an existing host, add its data before moving to the next
            if host:
                data.append([host, os_details, ", ".join(ports), ", ".join(services)])
            # Reset for the new host
            host = line.split()[-1]
            os_details = "Unknown"
            ports = []
            services = []
        elif "OS details:" in line:
            os_details = line.split(":", 1)[1].strip()
        elif "/tcp" in line and "open" in line:
            parts = line.split()
            port = parts[0]
            service = parts[-1]
            ports.append(port)
            services.append(service)

    # Add the last host's data
    if host:
        data.append([host, os_details, ", ".join(ports), ", ".join(services)])

    # Format the parsed data into a table
    return format_table(data, headers)
