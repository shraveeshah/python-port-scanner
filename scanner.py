import socket
import sys
from datetime import datetime

def scan_ports(target, start_port, end_port):
    print("-" * 50)
    print(f"Scanning Target: {target}")
    print(f"Scanning started at: {datetime.now()}")
    print("-" * 50)

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()

    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
            open_ports.append(port)
        sock.close()

    if not open_ports:
        print("No open ports found.")
    else:
        print(f"\nTotal open ports found: {len(open_ports)}")

if __name__ == "__main__":
    target = input("Enter target IP or hostname: ")
    start = int(input("Enter start port: "))
    end = int(input("Enter end port: "))
    scan_ports(target, start, end)