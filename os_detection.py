import subprocess
from utils import validate_ip_range, convert_ip_range

def clean_output(raw_output):
    """Clean and format the raw Nmap output into a user-friendly format."""
    lines = raw_output.splitlines()
    output = []
    output.append(f"{'Host':<30} {'OS Detected':<50}")
    host = None
    os_detected = None

    for line in lines:
        if "Nmap scan report for" in line:
            if host:  # Add previous host's information before moving to the next
                output.append(f"{host:<30} {os_detected:<50}")
            host = line.split()[-1]
            os_detected = "Unknown"  # Default value

        elif "OS details:" in line:
            os_detected = line.split(":", 1)[1].strip()  # Extract detected OS

    # Add the last host's information
    if host:
        output.append(f"{host:<30} {os_detected:<50}")

    return "\n".join(output)

def os_detection():
    """Detect operating system of target IP range."""
    target = input("Enter the target IP range (e.g., 192.168.50.20-253): ")
    while not validate_ip_range(target):
        print("Invalid IP range format! Please use the correct format (e.g., 192.168.50.20-253).")
        target = input("Enter the target IP range (e.g., 192.168.50.20-253): ")

    target_full_range = convert_ip_range(target)
    command = f"nmap -O {target_full_range}"
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
