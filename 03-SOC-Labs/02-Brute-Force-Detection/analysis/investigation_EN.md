# Manual Investigation — SSH Brute-Force Detection

## 1. Analyzed Service

The service involved in the events is:

```text
SSH / sshd
```

---

## 2. Involved User Account

The user account observed in the events is:

```text
admin
```

---

## 3. Source IP Address

All analyzed authentication attempts originated from:

```text
192.0.2.50
```

This IP address belongs to a range reserved for documentation and examples, so it is used exclusively as part of this simulated laboratory.

---

## 4. Authentication Attempts

The following events were identified:

```text
5 failed attempts
1 successful attempt
```

The five failed attempts were followed by a successful authentication.

---

## 5. Event Timeline

The observed events were:

| Time | Result |
|---|---|
| 10:01:21 | Failed |
| 10:01:24 | Failed |
| 10:01:28 | Failed |
| 10:01:32 | Failed |
| 10:01:36 | Failed |
| 10:01:40 | Accepted |

The first event occurred at `10:01:21`, and the last event occurred at `10:01:40`.

The total observed time interval was:

```text
19 seconds
```

The intervals between events were:

```text
3 seconds
4 seconds
4 seconds
4 seconds
4 seconds
```

---

## 6. Observed Pattern

The following pattern was identified:

```text
5 failed attempts
       ↓
Same source IP address
       ↓
Same user account
       ↓
Short time interval
       ↓
1 successful authentication
```

This behavior represents a pattern that warrants further investigation due to the repeated failed attempts followed by a successful authentication.

---

## 7. Initial Assessment

One possible legitimate explanation is that the user forgot or repeatedly entered an incorrect password before successfully authenticating.

Another possibility is that the attempts are consistent with password guessing activity or a brute-force attack.

Based on the information available in this log, it is not possible to determine which hypothesis is correct.

---

## 8. Available Evidence

The evidence used in this investigation is limited to the following file:

```text
logs/ssh-auth.log
```

The main observed indicators are:

| Indicator | Value |
|---|---|
| Service | SSH / sshd |
| User | `admin` |
| Source IP | `192.0.2.50` |
| Failed attempts | 5 |
| Successful attempts | 1 |
| First event | `10:01:21` |
| Last event | `10:01:40` |
| Observed duration | 19 seconds |

---

## 9. Additional Information Required

To determine whether the activity was legitimate or malicious, additional information would be required, such as:

- Other authentication events.
- Activity history of the `admin` account.
- Information about the affected system.
- Additional SSH server logs.
- Network activity associated with the IP address.
- Connection history from the same IP address.
- Information about the user assigned to the account.
- Events occurring after the successful authentication.
- Potential account changes made after authentication.

---

## 10. Conclusion

The manual analysis identified five failed SSH authentication attempts followed by one successful authentication from the same IP address and using the same user account.

The pattern is potentially suspicious and justifies further investigation. However, the available evidence is insufficient to confirm that a brute-force attack occurred.

This investigation demonstrates the importance of distinguishing between:

```text
Observed Event
       ↓
Identified Pattern
       ↓
Hypothesis
       ↓
Further Investigation
       ↓
Evidence-Based Conclusion
```

This approach helps prevent the assumption that every anomalous behavior automatically represents a security incident.