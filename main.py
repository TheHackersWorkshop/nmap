import sys
from network_discovery import network_discovery
from port_scan import port_scan
from os_detection import os_detection
from service_version import service_version_detection
from aggressive_scan import aggressive_scan
from firewall_evasion import firewall_evasion
from traceroute import traceroute
from vulnerability_scan import vulnerability_scan
from utils import check_sudo

def display_help():
    """Display instructions for using the tool."""
    print("\n--- Help Instructions ---")
    print("Welcome to the Network Scanning Tool!")
    print("This tool allows you to perform various network scans using Nmap, including:")
    print("1. Network Discovery - Scan a network to detect live hosts.")
    print("2. Port Scan - Identify open ports on a target.")
    print("3. OS Detection - Detect the operating system of target hosts.")
    print("4. Service Version Detection - Detect versions of services running on hosts.")
    print("5. Aggressive Scan - Perform a detailed scan to gather in-depth information.")
    print("6. Firewall Evasion - Use decoy scans to bypass firewalls and avoid detection.")
    print("7. Traceroute - Trace the network path to a target.")
    print("8. Vulnerability Scan - Use Nmap scripts to identify vulnerabilities.")
    print("\nTo use any of these options, simply select the corresponding number when prompted.")
    print("Type '9' to exit the tool.\n")

def main_menu():
    """Main menu that interacts with the user."""
    while True:
        print("\n--- Main Menu ---")
        print("1. Network Discovery")
        print("2. Port Scan")
        print("3. OS Detection")
        print("4. Service Version Detection")
        print("5. Aggressive Scan")
        print("6. Firewall Evasion (Decoy Scan)")
        print("7. Traceroute")
        print("8. Vulnerability Scan")
        print("9. Help")
        print("10. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            network_discovery()
        elif choice == '2':
            port_scan()
        elif choice == '3':
            os_detection()
        elif choice == '4':
            service_version_detection()
        elif choice == '5':
            aggressive_scan()
        elif choice == '6':
            firewall_evasion()
        elif choice == '7':
            traceroute()
        elif choice == '8':
            vulnerability_scan()
        elif choice == '9':
            display_help()
        elif choice == '10':
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    check_sudo()  # Ensure the script is run with sudo permissions
    main_menu()
