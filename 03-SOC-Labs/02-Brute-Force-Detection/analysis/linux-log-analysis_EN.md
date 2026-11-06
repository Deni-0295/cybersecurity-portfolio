# Command-Line Security Log Analysis

## 1. Objective

The objective of this exercise was to develop foundational command-line skills for security log analysis.

The investigation focused on filtering authentication events, extracting relevant fields, counting repeated values, identifying patterns, and applying a basic detection threshold.

The exercise was performed using simulated SSH authentication logs.

---

## 2. Environment

- Operating system: macOS Terminal
- Log format: SSH authentication log
- Data source: simulated security events
- Analysis type: command-line log analysis
- Main tools: `grep`, `awk`, `sort`, `uniq`, `wc`, `head`, `tail`

> Note: macOS was used as the practice environment because many command-line tools used in this exercise are available in its Unix-like terminal environment. This does not mean macOS is Linux.

---

## 3. Commands Learned

### `wc -l`

Used to count the number of lines in a log.

```bash
wc -l logs/ssh-auth.log
```

Example result:

```text
6 logs/ssh-auth.log
```

### `grep`

Used to search for specific patterns inside logs.

```bash
grep "Failed password" logs/ssh-auth.log
```

This allows authentication failures to be isolated from the rest of the log.

### `grep -c`

Used to count matching lines.

```bash
grep -c "Failed password" logs/ssh-auth.log
```

Example result:

```text
5
```

### `awk`

Used to extract specific fields and apply conditions.

Example:

```bash
awk '{print $11}' logs/ssh-auth.log
```

In the simulated SSH log format used in this exercise, field `$11` contains the source IP address.

Another example:

```bash
awk '$3 > "10:01:35"' logs/ssh-auth.log
```

This filters events occurring after a specific time.

### `sort`

Used to order extracted values.

```bash
sort
```

It can be combined with other commands:

```bash
sort | uniq
```

### `uniq`

Used to remove repeated consecutive values.

```bash
sort | uniq
```

For counting repeated values:

```bash
sort | uniq -c
```

### Pipes `|`

Pipes allow the output of one command to become the input of another.

Example:

```bash
grep "Failed password" logs/ssh-auth.log | wc -l
```

This command:

1. Finds failed authentication events.
2. Counts the resulting lines.

---

## 4. Log Investigation

The first simulated log contained six SSH authentication events.

Observed results:

| Indicator | Result |
|---|---:|
| Total events | 6 |
| Failed authentications | 5 |
| Successful authentications | 1 |
| User | `admin` |
| Source IP | `192.0.2.50` |
| Time interval | 19 seconds |

The event sequence showed five failed authentication attempts followed by one successful authentication from the same source IP.

---

## 5. Multi-Source Investigation

A second simulated log was analyzed to practice working with multiple source IP addresses and user accounts.

The log contained:

- 13 total authentication events.
- 11 failed authentication attempts.
- 2 successful authentication attempts.
- 4 source IP addresses.
- 3 user accounts.

Failed authentication counts by IP:

| Source IP | Failed attempts |
|---|---:|
| `192.0.2.50` | 5 |
| `192.0.2.51` | 3 |
| `192.0.2.52` | 1 |
| `192.0.2.53` | 2 |
| **Total** | **11** |

The IP address `192.0.2.50` produced the highest number of failed authentication events, with five attempts.

---

## 6. Pattern Detection

A basic detection condition was created:

```bash
grep "Failed password" logs/multi-source-ssh.log | \
awk '{print $11}' | \
sort | \
uniq -c | \
sort -nr | \
awk '$1 >= 5'
```

The purpose of this command was to identify source IP addresses with five or more failed authentication attempts.

Example result:

```text
5 192.0.2.50
```

This should be considered a detection candidate rather than proof of malicious activity.

---

## 7. Investigation Methodology

The exercise followed a basic SOC investigation workflow:

```text
Raw logs
   ↓
Filter relevant events
   ↓
Extract fields
   ↓
Count and group values
   ↓
Identify patterns
   ↓
Apply detection condition
   ↓
Investigate the evidence
   ↓
Form a cautious conclusion
```

This approach reduces the amount of information that must be reviewed manually and helps focus the investigation on relevant events.

---

## 8. Security Interpretation

The presence of multiple failed authentication attempts from the same source IP can represent a potentially suspicious pattern.

However, the log alone does not establish that the activity was malicious.

Possible explanations may include:

- A legitimate user entering an incorrect password multiple times.
- A user forgetting part of their password.
- An application using incorrect credentials.
- An administrator performing a test.
- Password guessing or brute-force activity.

Additional evidence would be required to distinguish between these possibilities.

---

## 9. Limitations

This investigation has several limitations:

- The logs are simulated.
- The dataset is very small.
- No historical activity was available.
- No network telemetry was analyzed.
- No endpoint activity was available.
- No information about the ownership of the source IP was available.
- The detection threshold of five failed attempts was selected for learning purposes.

Therefore, the detection condition should not be considered a production SOC rule.

---

## 10. Skills Practiced

- Unix-like command-line tools.
- SSH authentication log analysis.
- `grep`.
- `awk`.
- `sort`.
- `uniq`.
- `uniq -c`.
- `wc`.
- `head`.
- `tail`.
- Pipes.
- Field extraction.
- Event counting.
- Pattern identification.
- Basic detection logic.
- Timeline analysis.
- Evidence-based investigation.

---

## 11. Conclusion

This exercise demonstrated how command-line tools can transform raw authentication logs into structured information for security analysis.

Instead of manually reviewing every line, commands were used to filter events, extract IP addresses and usernames, count repeated values, analyze timelines, and identify potentially suspicious authentication patterns.

The investigation also reinforced an important SOC principle: a suspicious pattern is an indicator for further investigation, not necessarily confirmation of an attack.

The next step is to apply these concepts to larger datasets and eventually reproduce similar analysis using SIEM technologies.