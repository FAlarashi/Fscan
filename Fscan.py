import socket
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# Define common ports to scan
common_ports = {
    20: 'FTP Data Transfer',
    21: 'FTP Control (Command)',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    69: 'TFTP',
    80: 'HTTP',
    110: 'POP3',
    119: 'NNTP',
    123: 'NTP',
    143: 'IMAP',
    161: 'SNMP',
    194: 'IRC',
    389: 'LDAP',
    443: 'HTTPS',
    445: 'SMB',
    465: 'SMTPS',
    514: 'Syslog',
    587: 'SMTP (with TLS)',
    993: 'IMAPS',
    995: 'POP3S',
    1080: 'SOCKS',
    1433: 'Microsoft SQL Server',
    1434: 'Microsoft SQL Monitor',
    1521: 'Oracle DB',
    1723: 'PPTP',
    3306: 'MySQL',
    3389: 'RDP',
    5432: 'PostgreSQL',
    5900: 'VNC',
    6379: 'Redis',
    8080: 'HTTP-Proxy',
    8443: 'HTTPS-Alt',
    9000: 'SonarQube',
    9200: 'Elasticsearch',
    10000: 'Webmin'
}

# Function to scan a single port
def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)  # Lower timeout for faster scanning
        result = s.connect_ex((target, port))
        if result == 0:
            service = common_ports.get(port, 'Unknown Service')
            print(f"Port {port}: Open - {service}")
        s.close()
    except socket.error as e:
        print(f"Socket error on port {port}: {e}")

# Main function
def main():
    print("=" * 60)
    print(f"░▒█▀▀▀░░░░█▀▀░█▀▄░█▀▀▄░█▀▀▄")
    print(f"░▒█▀▀░░▀▀░▀▀▄░█░░░█▄▄█░█░▒█")
    print(f"░▒█░░░░░░░▀▀▀░▀▀▀░▀░░▀░▀░░▀")
    print("=" * 60)
    print(f"Author: Fahd Alarashi")
    print(f"github.com/FAlarashi")
    print("=" * 60)
    print(f"This tool is intended for educational purposes only. Unauthorized use of this tool to compromise systems is illegal and unethical. The author is not responsible for any misuse of the tool. Use it responsibly and only on systems you have permission to test.")
    print("=" * 60)
    target = input("Enter the target IP address: ")
    
    print("\nChoose the scan type:")
    print("1. Scan all ports (0-65535)")
    print("2. Scan common ports")
    print("3. Scan a range of ports")
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice not in {'1', '2', '3'}:
        print("Invalid choice. Exiting.")
        sys.exit()
    
    print("=" * 60)
    print(f"Scanning target {target}")
    print(f"Time started: {str(datetime.now())}")
    print("=" * 60)
    
    ports_to_scan = []

    try:
        if choice == '1':
            # Scan ports from 0 to 65535
            ports_to_scan = range(0, 65536)
        elif choice == '2':
            # Scan only common ports
            ports_to_scan = common_ports.keys()
        elif choice == '3':
            # Scan a range of ports specified by the user
            start_port = int(input("Enter the start port: "))
            end_port = int(input("Enter the end port: "))
            if 0 <= start_port <= 65535 and 0 <= end_port <= 65535 and start_port <= end_port:
                ports_to_scan = range(start_port, end_port + 1)
            else:
                print("Invalid port range. Exiting.")
                sys.exit()

        start_time = datetime.now()
        with ThreadPoolExecutor(max_workers=100) as executor:  # Use threading for faster scanning
            for port in ports_to_scan:
                executor.submit(scan_port, target, port)
        
        end_time = datetime.now()
        total_ports_scanned = len(ports_to_scan)
        time_taken = end_time - start_time
        print("=" * 60)
        print(f"Scanning completed.")
        print(f"Total ports scanned: {total_ports_scanned}")
        print(f"Time taken: {time_taken}")
        print("=" * 60)
    
    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()

    except socket.gaierror:
        print("\nHostname could not be resolved.")
        sys.exit()

    except socket.error:
        print("\nCouldn't connect to server.")
        sys.exit()

if __name__ == "__main__":
    main()

