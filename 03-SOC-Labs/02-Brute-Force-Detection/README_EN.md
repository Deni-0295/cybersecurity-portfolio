# SSH Brute Force Detection

## 1. Objective

The objective of this laboratory is to analyze SSH authentication events and identify potentially suspicious patterns in login attempts.

The investigation focuses on the source IP address, the user account involved, authentication results, and the time interval between events.

The laboratory also demonstrates how Python can be used to automate security log analysis.

---

## 2. Scenario

The simulated log `ssh-auth.log` contains SSH authentication events involving the user `admin` and the source IP address `192.0.2.50`.

The observed events are:

- 5 failed authentication attempts.
- 1 successful authentication attempt.
- All events originated from the same IP address.
- The events occurred within a short period of time.
- The first event occurred at `10:01:21`.
- The last event occurred at `10:01:40`.
- The total interval was 19 seconds.

The successful authentication occurred on the sixth attempt.

---

## 3. Manual Investigation

The initial investigation identified a pattern of repeated failed SSH authentication attempts followed by a successful authentication from the same IP address and user account.

This pattern may be consistent with password guessing or brute-force activity. However, the available log data alone is not sufficient to determine whether the activity was malicious or legitimate.

One possible legitimate hypothesis is that the user repeatedly entered an incorrect password before successfully authenticating.

Further investigation would be required to determine the nature of the activity.

---

## 4. Python Automation

The `analyze_logs.py` script automates the initial analysis of the SSH authentication log.

The script performs the following operations:

1. Locates the log file.
2. Reads the log line by line.
3. Identifies `Failed` and `Accepted` authentication events.
4. Extracts the username.
5. Extracts the source IP address.
6. Counts failed and successful authentication attempts by IP.
7. Calculates the interval between the first and last event.
8. Generates an alert when an IP address has 5 or more failed authentication attempts.

---

## 5. Detection Logic

For this laboratory, the detection rule is:

```text
5 or more failed authentication attempts
from the same source IP address.
```

When this condition is met, the script generates an alert for further investigation.

This threshold is used as a learning exercise and does not by itself confirm a brute-force attack.

---

## 6. Results

The automated analysis of `ssh-auth.log` identified:

| Field | Result |
|---|---|
| Service | SSH / sshd |
| Username | `admin` |
| Source IP | `192.0.2.50` |
| Failed attempts | 5 |
| Successful attempts | 1 |
| First event | `10:01:21` |
| Last event | `10:01:40` |
| Total interval | 19 seconds |
| Alert | 5 failed attempts detected |

### Additional Analysis: Multiple Sources

The `multi-source-ssh.log` file was used to expand the analysis to multiple source IP addresses and user accounts.

Results:

- 13 authentication events.
- 11 failed authentication attempts.
- 2 successful authentication attempts.
- 4 source IP addresses.
- 3 user accounts.

The IP address `192.0.2.50` generated the highest number of failed attempts, with 5.

---

## 7. Limitations

This laboratory uses simulated SSH authentication logs.

The analysis is intentionally simple and is designed to demonstrate the fundamentals of log processing and basic detection logic.

A real SOC investigation would require additional information, such as:

- Additional authentication events.
- Source host information.
- User activity.
- Authentication methods.
- Other system logs.
- Network telemetry.
- Historical activity from the source IP address.
- Additional evidence to determine whether the activity was malicious or legitimate.

---

## 8. Skills Developed

This laboratory helped develop foundational practical skills in:

- SSH authentication log analysis.
- Event correlation.
- IP address and user identification.
- Authentication event classification.
- Basic timeline analysis.
- Python log parsing.
- Regular expressions.
- Event counting and filtering.
- Basic detection logic.
- Security investigation documentation.

---

## 9. Laboratory Structure

```text
02-Brute-Force-Detection/
├── analysis/
│   ├── investigation_EN.md
│   ├── investigation.md
│   └── linux-log-analysis.md
├── logs/
│   ├── multi-source-ssh.log
│   └── ssh-auth.log
├── scripts/
│   └── analyze_logs.py
├── README_.md
└── README_EN.md
```

---

## 10. Conclusion

This laboratory demonstrates how security logs can be analyzed manually and then processed automatically using Python.

The objective is not to automatically classify an event as an attack, but to identify a potentially suspicious authentication pattern and generate an alert for further investigation by a security analyst.