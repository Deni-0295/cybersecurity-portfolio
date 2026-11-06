# Command-Line Security Log Analysis

## 1. Objective

The objective of this exercise was to develop foundational command-line skills for security log analysis.

The investigation focused on filtering authentication events, extracting relevant fields, counting repeated values, identifying patterns, and applying a basic detection threshold.

The exercise was performed using simulated SSH authentication logs.

---

## 2. Environment

- **Operating system:** macOS Terminal.
- **Log format:** SSH authentication log.
- **Data source:** Simulated security events.
- **Analysis type:** Command-line log analysis.
- **Main tools:** `grep`, `awk`, `sort`, `uniq`, `wc`, `head`, `tail`.

> Note: macOS was used as the practice environment because many command-line tools used in this exercise are available in its Unix-like terminal environment. This does not mean macOS is Linux.

---

## 3. Commands Learned

### `wc -l`

Used to count the number of lines in a log file.

```bash
wc -l logs/ssh-auth.log
```

Example result:

```text
6 logs/ssh-auth.log
```

### `grep`

Used to search for specific patterns inside log files.

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

Used to sort extracted values.

```bash
sort
```

It can also be combined with other commands:

```bash
sort | uniq
```

### `uniq`

Used to remove consecutive duplicate values.

```bash
sort | uniq
```

To count repeated values:

```bash
sort | uniq -c
```

### Pipes (`|`)

Pipes allow the output of one command to become the input of another.

Example:

```bash
grep "Failed password" logs/ssh-auth.log | wc -l
```

This command performs two actions:

1. Finds failed authentication events.
2. Counts the resulting lines.

---

## 4. Log Investigation

The first simulated log contained six SSH authentication events.

**Observed results:**

| Indicator | Result |
|---|---:|
| Total events | 6 |
| Failed authentications | 5 |
| Successful authentications | 1 |
| User | `admin` |
| Source IP address | `192.0.2.50` |
| Time interval | 19 seconds |

The event sequence showed five failed authentication attempts followed by one successful login from the same source IP address.

---

## 5. Multi-Source Investigation

A second simulated log was analyzed to practice working with multiple source IP addresses and user accounts.

The log contained:

- 13 total authentication events.
- 11 failed authentication attempts.
- 2 successful authentication attempts.
- 4 source IP addresses.
- 3 user accounts.

**Failed authentication attempts by source IP:**

| Source IP address | Failed attempts |
|---|---:|
| `192.0.2.50` | 5 |
| `192.0.2.51` | 3 |
| `192.0.2.52` | 1 |
| `192.0.2.53` | 2 |
| **Total** | **11** |

The IP address `192.0.2.50` generated the highest number of failed authentication events, with five attempts.

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

This result should be considered a detection candidate rather than proof of malicious activity.

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

The presence of multiple failed authentication attempts from the same source IP address may represent a potentially suspicious pattern.

However, the logs alone do not establish that the activity was malicious.

Possible explanations include:

- A legitimate user entering an incorrect password multiple times.
- A user forgetting part of their password.
- An application using incorrect credentials.
- An administrator performing a test.
- Password guessing or brute-force activity.

