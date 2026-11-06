import re
import ipaddress

from pathlib import Path
from collections import Counter
from datetime import datetime, timedelta


# CONFIGURATION
SCRIPT_DIR = Path(__file__).resolve().parent

LOG_FILE = SCRIPT_DIR.parent / "logs" / "ssh-auth.log"
EVIDENCE_DIR = SCRIPT_DIR.parent / "evidence"

DETECTION_THRESHOLD = 5


# DATA STORAGE
failed_by_ip = Counter()
accepted_by_ip = Counter()
failed_by_user = Counter()

events = []
event_times = []


# REGEX PATTERNS
auth_pattern = re.compile(
    r"(Failed password|Accepted password) "
    r"for (?:invalid user )?(\S+) "
    r"from (\d{1,3}(?:\.\d{1,3}){3})"
)

time_pattern = re.compile(r"\b(\d{2}:\d{2}:\d{2})\b")


# LOG ANALYSIS
print(f"Analyzing: {LOG_FILE}")

if not LOG_FILE.exists():
    raise FileNotFoundError(f"Log file not found: {LOG_FILE}")

with LOG_FILE.open("r", encoding="utf-8") as file:

    for line in file:

        match = auth_pattern.search(line)

        if not match:
            continue

        result = (
            "Failed"
            if match.group(1) == "Failed password"
            else "Accepted"
        )

        username = match.group(2)
        source_ip = match.group(3)

        # Validate source IP
        try:
            ipaddress.ip_address(source_ip)
        except ValueError:
            continue

        # Extract event time
        time_match = time_pattern.search(line)

        event_time = None

        if time_match:
            event_time = datetime.strptime(
                time_match.group(1),
                "%H:%M:%S"
            )

            event_times.append(event_time)

        event = {
            "result": result,
            "username": username,
            "source_ip": source_ip,
            "time": event_time
        }

        events.append(event)

        # Count authentication attempts
        if result == "Failed":
            failed_by_ip[source_ip] += 1
            failed_by_user[username] += 1

        else:
            accepted_by_ip[source_ip] += 1


# EVENT OUTPUT
print("\nAUTHENTICATION EVENTS")

for event in events:

    print(f"Result: {event['result']}")
    print(f"Username: {event['username']}")
    print(f"Source IP: {event['source_ip']}")


# IP SUMMARY
summary_lines = [
    "SSH AUTHENTICATION SUMMARY",
    "--------------------------"
]

all_ips = sorted(set(failed_by_ip) | set(accepted_by_ip))

for ip in all_ips:

    summary_lines.extend([
        "",
        f"IP: {ip}",
        f"Failed attempts: {failed_by_ip[ip]}",
        f"Successful attempts: {accepted_by_ip[ip]}"
    ])

print("\n SUMMARY ")
print("\n".join(summary_lines))


# USER SUMMARY


print("\n FAILED ATTEMPTS BY USER ")

for username, count in failed_by_user.items():
    print(f"{username}: {count}")


# EVENT TIMELINE


timeline_lines = ["EVENT TIMELINE"]

if event_times:

    first_event = event_times[0]
    last_event = event_times[-1]

    duration = last_event - first_event

    # Handle events crossing midnight
    if duration.total_seconds() < 0:
        duration += timedelta(days=1)

    timeline_lines.extend([
        f"First event: {first_event.strftime('%H:%M:%S')}",
        f"Last event: {last_event.strftime('%H:%M:%S')}",
        f"Total interval: {duration.total_seconds():.0f} seconds"
    ])

    print("\n EVENT INTERVAL ")
    print("\n".join(timeline_lines))

else:
    timeline_lines.append("No event timestamps found.")


# ALERT DETECTION


alert_lines = ["BRUTE FORCE DETECTION RESULTS"]

for ip, failed_count in failed_by_ip.items():

    if failed_count >= DETECTION_THRESHOLD:

        alert_lines.append(
            f"ALERT: {ip} has {failed_count} "
            "failed authentication attempts."
        )

if len(alert_lines) == 1:
    alert_lines.append("No detection threshold reached.")

print("\n ALERTS ")
print("\n".join(alert_lines))


# EVIDENCE GENERATION
EVIDENCE_DIR.mkdir(exist_ok=True)

# Evidence 1: Failed authentication attempts
failed_lines = [
    "FAILED SSH AUTHENTICATION EVENTS",
    "--------------------------------"
]

for event in events:

    if event["result"] == "Failed":

        time_value = (
            event["time"].strftime("%H:%M:%S")
            if event["time"]
            else "Unknown"
        )

        failed_lines.append(
            f"{time_value} | User: {event['username']} "
            f"| Source IP: {event['source_ip']}"
        )

# Evidence 2: IP analysis
ip_analysis_lines = [
    "SOURCE IP ANALYSIS",
    "------------------"
]

for ip in all_ips:

    ip_analysis_lines.extend([
        "",
        f"Source IP: {ip}",
        f"Failed attempts: {failed_by_ip[ip]}",
        f"Successful attempts: {accepted_by_ip[ip]}"
    ])

# Evidence 3: Detection report
detection_lines = (
    summary_lines
    + [""]
    + timeline_lines
    + [""]
    + alert_lines
)

evidence_files = {
    "failed-attempts.txt": failed_lines,
    "ip-analysis.txt": ip_analysis_lines,
    "detection-results.txt": detection_lines
}

for filename, content in evidence_files.items():

    output_file = EVIDENCE_DIR / filename

    output_file.write_text(
        "\n".join(content) + "\n",
        encoding="utf-8"
    )

    print(f"Evidence saved: {output_file}")

print("\nAnalysis completed successfully.")
