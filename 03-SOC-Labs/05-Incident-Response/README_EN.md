[Versión español](README.md)

# Laboratory 05 — Incident Response

## Description

This Laboratory involved a simulated investigation of a security incident related to suspicious PowerShell activity.

The incident began with an alert on host `PC-023`, where a suspicious relationship between Microsoft Word and PowerShell was observed:

```text
winword.exe → powershell.exe
```

Further investigation revealed script execution, network communication, and the creation of an executable file.

The investigation identified the same suspicious document on multiple hosts, which led to an expansion of the incident scope.

---

## Objectives

- Analyze a security alert.
- Investigate process relationships.
- Build an incident timeline.
- Identify Indicators of Compromise (IOCs).
- Determine the scope of an incident.
- Prioritize affected hosts.
- Develop an initial access hypothesis.
- Apply containment measures.
- Preserve evidence.
- Perform threat hunting.
- Distinguish between exposure and confirmed compromise.

---

## Alert Summary

| Field | Value |
|---|---|
| Case ID | SOC-CASE-001 |
| Severity | High |
| Initial Host | PC-023 |
| User | employee |
| Process | powershell.exe |
| Parent Process | winword.exe |
| Script | update.ps1 |
| Network IP | 198.51.100.25 |
| Created File | invoice_update.exe |

---

## Main Process Chain

```text
Phishing Email
      ↓
invoice.docm
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

---

## Key Findings

### PC-023

The strongest evidence was observed on `PC-023`.

Observed activities included:

- `winword.exe → powershell.exe`
- `ExecutionPolicy Bypass`
- Execution of `update.ps1`
- Network connection to `198.51.100.25`
- Creation of `invoice_update.exe`

**Assessment:** High risk / potential compromise.

### PC-017

Observed process relationship:

```text
winword.exe → powershell.exe
```

The same suspicious `invoice.docm` file and hash were identified.

**Assessment:** Suspicious activity / further investigation required.

### PC-041

Observed process relationship:

```text
winword.exe → powershell.exe
```

The same suspicious `invoice.docm` file and hash were identified.

**Assessment:** Suspicious activity / further investigation required.

### PC-078

The suspicious `invoice.docm` file was present, but no PowerShell activity was detected.

**Assessment:** Potentially exposed / monitoring required.

---

## Indicators of Compromise (IOCs)

```text
File:
invoice.docm

Hash (provided):
9f86d081884c7d659a2feaa0c55ad015

PowerShell Script:
update.ps1

Created Executable:
invoice_update.exe

IP Address:
198.51.100.25

Process Relationship:
winword.exe → powershell.exe
```

---

## Initial Access Hypothesis

The primary hypothesis is that the incident originated from a phishing email containing the file `invoice.docm`.

The email may have used social engineering techniques and urgency to persuade users to open the document.

```text
Phishing
    ↓
Social Engineering
    ↓
invoice.docm
    ↓
Microsoft Word
    ↓
PowerShell
    ↓
Payload
```

The same document hash was identified on multiple systems, suggesting that the file may have been distributed to several users.

---

## Incident Response

The main response actions considered during the investigation were:

1. **Containment**
   - Isolate suspicious hosts from the network.

2. **Evidence Preservation**
   - Preserve suspicious files, logs, email information, and network evidence.

3. **Threat Hunting**
   - Search the environment for known hashes, filenames, IP addresses, and suspicious process relationships.

4. **Email Containment**
   - Identify and remove the phishing email from affected mailboxes.

5. **Eradication**
   - Quarantine and remove confirmed malicious artifacts after preserving the necessary evidence.

6. **Recovery**
   - Restore systems to a trusted state and monitor them after recovery.

7. **Post-Incident Monitoring**


---

## Evidence

```text
evidence/
├── alert.txt
├── timeline.txt
├── process-tree.txt
├── indicators.txt
├── affected-hosts.txt
└── response-actions.txt
```

Detailed investigation:

```text
investigation.md
```

---

## Skills Practiced

- Incident Response
- Alert Triage
- Process Tree Analysis
- PowerShell Investigation
- IOC Identification
- Threat Hunting
- Timeline Reconstruction
- Incident Scoping
- Host Prioritization
- Containment
- Evidence Preservation
- Phishing Investigation
- Social Engineering Analysis

---

### Summary

The investigation identified a potential phishing-based attack involving a macro-enabled Microsoft Word document.

The suspected execution chain was:

```text
Phishing Email
      ↓
invoice.docm
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

The strongest evidence was found on `PC-023`, while `PC-017` and `PC-041` required further investigation.

`PC-078` was considered potentially exposed because the suspicious file was present, but no execution was detected.

Copyright (c) 2026 Irma (Deni-0295). Todos los derechos reservados.

Este repositorio y su contenido (reportes, documentos, imágenes y textos)
son propiedad de la autora. No se permite copiar, modificar, distribuir
ni utilizar este material, total o parcialmente, sin autorización
previa y por escrito.