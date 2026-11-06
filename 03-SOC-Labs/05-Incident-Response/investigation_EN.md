# Laboratorio 05 — Incident Response Investigation

## 1. Incident Information

**Case ID:** SOC-CASE-001
**Severity:** High
**Initial Host:** PC-023
**User:** employee
**Detected Activity:** Suspicious PowerShell Activity

The incident began with an alert related to suspicious PowerShell activity.

The observed process relationship was:

```text
winword.exe → powershell.exe
```

The executed command was:

```text
powershell.exe -ExecutionPolicy Bypass -File C:\Users\employee\AppData\Temp\update.ps1
```

---

## 2. Initial Analysis

Several relevant indicators were identified:

* Microsoft Word spawned PowerShell.
* PowerShell used `-ExecutionPolicy Bypass`.
* The `update.ps1` script was executed.
* The script was located under `AppData\Temp`.
* PowerShell established a network connection.
* PowerShell subsequently created `invoice_update.exe`.

The combination of these events significantly increased the level of suspicion.

---

## 3. Process Tree

The main execution chain was:

```text
winword.exe
    │
    └── powershell.exe
            │
            ├── update.ps1
            │
            ├── Network Connection
            │       └── 198.51.100.25
            │
            └── invoice_update.exe
```

The `winword.exe → powershell.exe` relationship was considered suspicious because Microsoft Word normally does not need to launch PowerShell during normal document processing.

---

## 4. Timeline

```text
10:13:58  employee opened invoice.docm
10:14:01  winword.exe started
10:14:31  winword.exe spawned powershell.exe
10:14:32  powershell.exe executed update.ps1
10:14:35  powershell.exe connected to 198.51.100.25
10:14:37  powershell.exe created invoice_update.exe
```

---

## 5. Scope Investigation

Additional hosts containing the same document were identified:

```text
PC-023 → invoice.docm
PC-017 → invoice.docm
PC-041 → invoice.docm
PC-078 → invoice.docm
```

All hosts contained the same hash:

```text
9f86d081884c7d659a2feaa0c55ad015
```

This indicates that the same file content was present on multiple hosts.

PC-017 and PC-041 also showed:

```text
winword.exe → powershell.exe
```

PC-078 contained the file, but no PowerShell execution was observed.

Therefore, PC-078 was classified as potentially exposed rather than confirmed compromised.

---

## 6. Host Prioritization

Hosts were prioritized according to the available evidence:

```text
1. PC-023 → HIGH RISK / POTENTIAL COMPROMISE
2. PC-009 → HIGH PRIORITY INVESTIGATION
3. PC-017 → SUSPICIOUS / REQUIRES INVESTIGATION
4. PC-041 → SUSPICIOUS / REQUIRES INVESTIGATION
5. PC-078 → EXPOSED / MONITOR
```

PC-023 presented the strongest evidence.

PC-009 received high priority because it involved an administrative account and the unusual process relationship:

```text
chrome.exe → powershell.exe
```

PC-017 and PC-041 presented the same Word-to-PowerShell pattern.

PC-078 only showed the suspicious file without evidence of execution.

---

## 7. Initial Access Hypothesis

The primary hypothesis is that the incident originated from a phishing email.

The message used social engineering to create urgency:

```text
Subject: Urgent Invoice 2026
Attachment: invoice.docm
```

The filename could make the document appear legitimate.

The `.docm` extension indicates a Microsoft Word macro-enabled document.

The suspected attack chain is:

```text
Phishing Email
      ↓
invoice.docm
      ↓
User opens document
      ↓
winword.exe
      ↓
powershell.exe
      ↓
update.ps1
      ↓
Network Connection
      ↓
invoice_update.exe
```

This hypothesis should be validated through additional analysis of the email, document, script, and host artifacts.

---

## 8. Incident Response

### Containment

* Isolate PC-023, PC-017, and PC-041 from the network.
* Prevent additional communication with suspicious infrastructure.
* Reduce the risk of propagation or lateral movement.

### Evidence Preservation

Preserve:

* `invoice.docm`
* `update.ps1`
* `invoice_update.exe`
* PowerShell logs
* Process creation logs
* Network logs
* Email headers
* Original phishing email

Immediate deletion of suspicious files should be avoided until relevant evidence has been preserved.

### Threat Hunting

Search the environment for:

```text
SHA-256:
9f86d081884c7d659a2feaa0c55ad015

IP:
198.51.100.25

Files:
invoice.docm
update.ps1
invoice_update.exe
```

Also search for:

```text
winword.exe → powershell.exe
```

### Eradication

After evidence preservation and analysis:

* Quarantine confirmed malicious files.
* Remove confirmed malicious artifacts.
* Check for persistence mechanisms.
* Validate that no additional malicious components remain.

### Recovery

* Restore affected systems to a trusted state.
* Validate systems before reconnecting them.
* Continue monitoring after recovery.

---

## 9. Incident Assessment

The incident shows characteristics consistent with a potential phishing attack followed by PowerShell execution.

The main risk factors were:

* `.docm` document.
* Distribution to multiple users.
* Same file hash across multiple hosts.
* `winword.exe → powershell.exe`.
* `ExecutionPolicy Bypass`.
* Script execution from `AppData\Temp`.
* Network communication.
* Executable creation.

The available evidence supports a **high suspicion of compromise on PC-023** and requires further investigation of PC-017 and PC-041.

PC-078 is considered potentially exposed but is not confirmed compromised based on the currently available evidence.
