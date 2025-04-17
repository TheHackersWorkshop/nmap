import subprocess
import re
import sys
import time
from utils import get_local_network

def clean_output(raw_output):
    """Clean and format the raw Nmap output into a user-friendly format."""
    lines = raw_output.splitlines()
    output = []
    output.append(f"{'Host':<30} {'Status':<10} {'Additional Info':<20}")
    up_count = 0
    host = None

    for line in lines:
        if "Nmap scan report for" in line:
            host = line.split()[-1]
        elif "Host is up" in line:
            status = "Up"
            output.append(f"{host:<30} {status:<10} {'':<20}")
            up_count += 1
        elif "Host is down" in line:
            status = "Down"
            output.append(f"{host:<30} {status:<10} {'':<20}")

    summary = f"\nScan complete. Found {up_count} hosts up."
    return "\n".join(output) + summary

def validate_network_range(network):
    """Validate the network range format (e.g., 192.168.50.0/24)."""
    pattern = re.compile(r"(\d{1,3}\.){3}\d{1,3}/\d{1,2}")
    return bool(pattern.match(network))

def network_discovery():
    """Discover the local network and offer the user an option to change it."""
    default_network = get_local_network()
    if default_network:
        print(f"Default Network Detected: {default_network}")
        change_network = input("Do you want to change the network range (y/n)? ")
        if change_network.lower() == 'y':
            network = input("Enter the new network range (e.g., 192.168.50.0/24): ")
            while not validate_network_range(network):
                print("Invalid network range format! Please use the correct format (e.g., 192.168.50.0/24).")
                network = input("Enter the new network range (e.g., 192.168.50.0/24): ")
        else:
            network = default_network
    else:
        network = input("Enter the network range to scan (e.g., 192.168.50.0/24): ")
        while not validate_network_range(network):
            print("Invalid network range format! Please use the correct format (e.g., 192.168.50.0/24).")
            network = input("Enter the network range to scan (e.g., 192.168.50.0/24): ")

    command = f"nmap -sP {network}"
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

