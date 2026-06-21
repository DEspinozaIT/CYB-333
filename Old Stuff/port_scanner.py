#!/usr/bin/env python3
"""Beginner port scanner for localhost and scanme.nmap.org."""

import socket
import time

print("Port Scanner")
print("Only scan localhost or scanme.nmap.org")

while True:
    host = input("Host (leave blank for localhost): ").strip()
    if not host:
        host = "localhost"
    if "port_scanner.py" in host or "python3" in host or "./" in host or "/" in host:
        print("Enter only the host name, for example localhost.")
        continue
    break

try:
    start_port = int(input("Start port (for example 1): ").strip() or "1")
    end_port = int(input("End port (for example 100): ").strip() or "100")
except ValueError:
    print("Please enter valid numbers for ports.")
    raise SystemExit(1)

if start_port < 1 or end_port > 65535 or start_port > end_port:
    print("Please use a valid port range from 1 to 65535.")
    raise SystemExit(1)

if host not in ("localhost", "127.0.0.1", "scanme.nmap.org"):
    print("Warning: only scan localhost or scanme.nmap.org.")

try:
    target = socket.gethostbyname(host)
except socket.gaierror:
    print("Could not resolve the host.")
    raise SystemExit(1)

print("Scanning {} ({}) from {} to {}".format(host, target, start_port, end_port))
open_ports = []

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1.0)
    try:
        result = sock.connect_ex((target, port))
        if result == 0:
            print("Port {}: OPEN".format(port))
            open_ports.append(port)
        else:
            print("Port {}: closed".format(port))
    except socket.error:
        print("Port {}: error".format(port))
    finally:
        sock.close()
    time.sleep(0.1)

print("\nScan complete.")
if open_ports:
    print("Open ports:", open_ports)
else:
    print("No open ports found.")
