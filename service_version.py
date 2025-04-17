import subprocess
from utils import validate_ip_range, convert_ip_range

def clean_output(raw_output):
    """Clean and format the raw Nmap output into a user-friendly format."""
    lines = raw_output.splitlines()
    output = []
    output.append(f"{'Host':<30} {'Port':<10} {'Service':<20} {'Version':<30}")
    host = None

    for line in lines:
        if "Nmap scan report for" in line:
            host = line.split()[-1]
        elif "open" in line:
            parts = line.split()
            port = parts[0]  # Port number and protocol (e.g., 22/tcp)
            service = parts[2]  # Service name (e.g., ssh)
            version = " ".join(parts[3:]) if len(parts) > 3 else "Unknown"  # Version info if available
            output.append(f"{host:<30} {port:<10} {service:<20} {version:<30}")

    return "\n".join(output)

def service_version_detection():
    """Detect service versions running on the target IP range."""
    target = input("Enter the target IP range (e.g., 192.168.50.20-253): ")
    while not validate_ip_range(target):
        print("Invalid IP range format! Please use the correct format (e.g., 192.168.50.20-253).")
        target = input("Enter the target IP range (e.g., 192.168.50.20-253): ")

    target_full_range = convert_ip_range(target)  # Convert to full IP range
    command = f"nmap -sV {target_full_range}"
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
