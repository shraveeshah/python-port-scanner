Python Port Scanner

A lightweight command-line port scanner built with Python's `socket` library.  
Designed to identify open TCP ports on a target host — a foundational tool in network security and ethical hacking.

---

Motivation

Understanding which ports are open on a system is the first step in network reconnaissance.  
This project was built to learn the basics of socket programming and TCP/IP communication.

---

How It Works

- Resolves hostname to IP
- Iterates through a given port range
- Attempts a TCP connection on each port
- Reports open ports with timestamps

---

Usage

```bash
python scanner.py
```

Enter the target IP and port range when prompted.

Only scan systems you own or have explicit permission to scan.

---

Concepts Covered

- TCP/IP basics
- Socket programming in Python
- Network reconnaissance fundamentals
- Ethical hacking methodology

---

Future Improvements

- Add UDP scanning
- Add service/banner detection
- Export results to a file
- Add multithreading for faster scans

---

Author

Shravee | IT Student at MKSSS's Cummins College of Engineering for Women  
Interested in Web Security, Ethical Hacking & Network Security
