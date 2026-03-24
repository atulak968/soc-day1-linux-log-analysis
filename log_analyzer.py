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
