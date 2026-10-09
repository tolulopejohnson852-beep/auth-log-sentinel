from collections import Counter

LOG_FILE = "sample_logs/auth.log"

failed_counts = Counter()

with open(LOG_FILE) as log:
    for line in log:
        parts = line.split()
        if len(parts) != 5:
            continue
        date, time, status, user, ip = parts
        if status == "FAILED":
            failed_counts[ip] += 1

print("Failed logins per IP:")
for ip, count in failed_counts.most_common():
    print(f"{ip}: {count}")
