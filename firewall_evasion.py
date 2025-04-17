import subprocess
from utils import validate_ip_range, convert_ip_range

def firewall_evasion():
    """Perform a decoy scan to evade firewalls."""
    target = input("Enter the target IP range (e.g., 192.168.50.20-253): ")
    while not validate_ip_range(target):
        print("Invalid IP range format! Please use the correct format (e.g., 192.168.50.20-253).")
        target = input("Enter the target IP range (e.g., 192.168.50.20-253): ")

    target_full_range = convert_ip_range(target)  # Convert to full IP range
    command = f"nmap -D RND:10 {target_full_range}"
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
    output = []
    output.append(f"{'Host':<30} {'Status':<10} {'Is Decoy':<10}")

    # Parsing the Nmap output
    host = None
    status = "Unknown"
    is_decoy = "No"

    for line in lines:
        if "Nmap scan report for" in line:
            if host:  # Save the previous host info before moving to the next
                output.append(f"{host:<30} {status:<10} {is_decoy:<10}")
            host = line.split()[-1]
            status = "Unknown"
            is_decoy = "No"  # Default is not a decoy

        elif "Host is up" in line:
            status = "Up"
        elif "Host is down" in line:
            status = "Down"

        elif "Using decoy" in line:  # Identify decoy hosts
            is_decoy = "Yes"

    # Add the last host's info
    if host:
        output.append(f"{host:<30} {status:<10} {is_decoy:<10}")

    return "\n".join(output)
