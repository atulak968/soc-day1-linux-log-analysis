🛡️ Day 1 – Linux Authentication Log Analysis

📌 Objective:This project focuses on analyzing Linux authentication logs to detect brute-force login attempts and identify suspicious IP addresses using both manual investigation and Python automation.

🧠 Skills Learned:
Log analysis (Linux auth logs)
Brute force attack detection
Command line tools (grep, awk, sort, uniq)
Python log parsing
SOC investigation mindset

📂 Log Sample:
Mar 24 10:01:23 server sshd[1234]: Failed password for root from 192.168.1.10 port 22 ssh2
Mar 24 10:01:25 server sshd[1235]: Failed password for admin from 192.168.1.10 port 22 ssh2
Mar 24 10:01:30 server sshd[1236]: Failed password for root from 192.168.1.11 port 22 ssh2
Mar 24 10:01:35 server sshd[1237]: Accepted password for user from 192.168.1.12 port 22 ssh2
Mar 24 10:01:40 server sshd[1238]: Failed password for root from 192.168.1.10 port 22 ssh2

🔍 Manual Analysis
Identified repeated failed login attempts
Detected suspicious IP: 192.168.1.10
Total attempts: 3
Attack type: Brute Force

Command Line Analysis:
grep "Failed password" auth.log
grep "Failed password" auth.log | awk '{print $(NF-3)}'
grep "Failed password" auth.log | awk '{print $(NF-3)}' | sort | uniq -c


Python Automation:
import re
from collections import defaultdict

log_file = "auth.log"
failed_attempts = defaultdict(int)

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
            if ip_match:
                ip = ip_match.group(1)
                failed_attempts[ip] += 1

for ip, count in failed_attempts.items():
    print(f"{ip} → {count}")



🚨 Incident Report
Attack Type: Brute Force
Source IP: 192.168.1.10
Attempts: 3
Target Accounts: root, admin
Severity: Medium

🎯 Conclusion

This project demonstrates how SOC analysts detect brute-force attacks using log analysis and basic automation techniques.

