# Nmap.py

This Python script provides a simple menu-driven interface for common Nmap (Network Mapper) functionalities on Linux. It allows users to easily execute various network scanning tasks without needing to remember specific Nmap command-line options.

## Features

The script offers the following Nmap options through a numbered menu:

1.  **Network Discovery:** Performs a basic ping scan to identify live hosts on a network.
2.  **Port Scan:** Scans specified target(s) for open ports using the SYN scan technique.
3.  **OS Detection:** Attempts to determine the operating system of the target host(s).
4.  **Service Version Detection:** Identifies the versions of services running on open ports.
5.  **Aggressive Scan:** Combines OS detection, version detection, script scanning, and traceroute for a comprehensive scan.
6.  **Firewall Evasion (Decoy Scan):** Attempts to evade firewalls by using decoy IP addresses in the scan.
7.  **Traceroute:** Displays the path taken by packets to reach the target host(s).
8.  **Vulnerability Scan:** Utilizes Nmap's scripting engine (NSE) to scan for known vulnerabilities.
9.  **Help:** Displays a brief description of each menu option.
10. **Exit:** Closes the program.

## Prerequisites

* **Linux Operating System:** This script is designed to run on Linux as it directly calls the `nmap` command.
* **Nmap Installed:** The `nmap` utility must be installed on your system. You can typically install it using your distribution's package manager (e.g., `sudo apt-get install nmap` on Debian/Ubuntu, `sudo yum install nmap` on CentOS/RHEL, `sudo pacman -S nmap` on Arch Linux).
* **Python 3:** This script is written in Python 3.

## Installation

1.  **Download the script:** You can download the `nmap-menu.py` file from your GitHub repository.

  
    git clone (https://github.com/TheHackersWorkshop/nmap)



2.  **Make it executable (optional but recommended):**

    chmod +x nmap-menu.py


## Usage

1.  **Open a terminal:** Navigate to the directory where you saved the `nmap-menu.py` file.

2.  **Run the script:**


    python3 main.py


3.  **Follow the menu:** The script will display the main menu with numbered options. Enter the number corresponding to the Nmap scan you want to perform and press Enter.

4.  **Provide target information:** The script will prompt you to enter the target IP address(es) or network range as required for the selected scan.

5.  **View the results:** The output of the Nmap command will be displayed in your terminal.

6.  **Return to the menu:** After the scan is complete, you will be presented with the main menu again to perform another scan or exit.
