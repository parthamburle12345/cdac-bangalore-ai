import re

# Define named groups using (?P<group_name>pattern)

def analyze_server_logs(logs_text):
    output = []
    for log in logs_text.splitlines():        
        log_pattern = r"""(?P<ip>[0-9.]+) - - (?P<time>[\[A-Za-z0-9/:\]]+)\s"(?P<method>[A-Z]+)\s/(?P<resource>[a-z0-9_./]+)\s(?P<http>[A-Z/.0-9]+)\"\s(?P<status>[0-9]+)\s(?P<bytes>[0-9]+)"""
        m = re.match(log_pattern,log)
        if m:
            # print(m.group('ip'))
            if re.search(r"192.168.[0-9.]+",m.group('ip')) or re.search(r"10.[0-9.]+",m.group('ip')):
                continue
            else:
                output.append(m.groupdict(0))
        else:
            print(f"Warning: Could not parse line: '{log}'. Skipping.\n")
    return output
        
log_data = """192.168.1.5 - - [28/Aug/2026:10:00:00] "GET /index.html HTTP/1.1" 200 1024
8.8.8.8 - - [28/Aug/2026:10:10:00] "GET /api/v1/users HTTP/1.1" 200 4096
Corrupted log entry here
10.0.0.12 - - [28/Aug/2026:10:15:00] "POST /submit_data HTTP/1.1" 403 512
172.16.0.4 - - [28/Aug/2026:10:20:00] "POST /login HTTP/1.1" 401 256"""

print("\n")
for item in analyze_server_logs(log_data):
    print("    {")
    for elem in item:
        print(f"\t{elem} : {item[elem]}")
    print("    },")