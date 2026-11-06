[Versión español](README.md)

# 03 | SOC LABS — SECURITY OPERATIONS CENTER LABORATORIES

**Practical laboratories focused on threat investigation, analysis, and detection**

## Overview

This section brings together hands-on laboratories designed to develop technical and analytical skills related to Security Operations Center (SOC) activities.

The goal is to learn how to identify suspicious activities, analyze security logs, investigate potential threats, recognize Indicators of Compromise (IOCs), and understand incident response processes.

Each laboratory documents its objectives, environment, tools, investigation procedures, collected evidence, and results.

All exercises are conducted in controlled environments for educational purposes.

---

## Laboratory Status

| Status | Description |
|---|---|
| 🟢 **Completed** | Laboratory completed and documented |
| 🔵 **In Progress** | Laboratory currently under development |
| ⚪ **Planned** | Laboratory not yet started |

---

## Laboratories

| Laboratory | Objective | Status |
|---|---|---|
| [01 - Log Analysis](./01-Log-Analysis/) | Identify log sources and analyze Linux events. | 🟢 Completed |
| [02 - Brute Force Detection](./02-Brute-Force-Detection/) | Investigate SSH authentication attempts and detect brute-force patterns. | 🟢 Completed |
| [03 - Phishing Analysis](./03-Phishing-Analysis/) | Analyze suspicious emails, headers, URLs, and phishing indicators. | 🟢 Completed |
| [04 - Malware Analysis](./04-Malware-Analysis/) | Investigate suspicious files and analyze potentially malicious behavior. | 🟢 Completed |
| [05 - Incident Response](./05-Incident-Response/) | Practice incident investigation, containment, and response procedures. | 🟢 Completed |
| [06 - SIEM Fundamentals](./06-SIEM-Fundamentals/) | Understand SIEM fundamentals, security monitoring, and event analysis. | 🔵 In Progress |

---

## Learning Objectives

Through these laboratories, I aim to develop the following skills:

- **Log Analysis:** Interpret authentication events, system activity, and security logs.
- **Threat Detection:** Identify suspicious patterns and potential Indicators of Compromise (IOCs).
- **Incident Investigation:** Collect, analyze, and correlate evidence.
- **Phishing Analysis:** Recognize social engineering techniques and fraudulent emails.
- **Malware Analysis:** Understand suspicious behavior and potential execution mechanisms.
- **Security Monitoring:** Learn how Security Information and Event Management (SIEM) platforms work.
- **Incident Response:** Understand the stages of identification, analysis, containment, and recovery.
- **Technical Documentation:** Prepare structured reports containing findings and conclusions.

---

## Tools and Technologies

The tools used or planned for this learning path include:

| Category | Tools |
|---|---|
| Operating Systems | Kali Linux, Linux, and Windows |
| Log Analysis | journalctl, grep, awk |
| Networking | Wireshark |
| Programming | Python, Bash, and PowerShell |
| SIEM | Wazuh, Splunk, and Elastic Security |
| Detection | Sigma and YARA |
| Threat Intelligence | IP address, domain, URL, and hash analysis sources |
| Frameworks | MITRE ATT&CK |
| Documentation | Git and GitHub |

*Each laboratory specifies the tools that were actually used.*

---

## Investigation Methodology

The laboratories follow a workflow based on common SOC investigation activities:

1. **Objective Definition:** Identify the security activity or issue to be investigated.
2. **Environment Preparation:** Configure the required systems and tools.
3. **Evidence Collection:** Gather relevant logs, events, files, and indicators.
4. **Analysis:** Examine the information and identify suspicious behavior.
5. **Correlation:** Relate events and evidence to understand what happened.
6. **Classification:** Determine the findings and their potential impact.
7. **Documentation:** Record the procedures, evidence, and results.
8. **Conclusion:** Present the findings and possible recommended actions.

---

## Laboratory Structure

Depending on the requirements of each exercise, every laboratory will follow an organization similar to the structure below:

```text
XX-Lab-Name/
│
├── README.md
│
├── evidence/
│   ├── evidence-files.txt
│   └── analysis-results.txt
│
├── investigation.md
│
└── screenshots/
```

**File Descriptions:**

- `README.md`: Introduces the laboratory, its objectives, and the tools used.
- `evidence/`: Stores the files and results collected during the investigation.
- `investigation.md`: Documents the procedures, analysis, findings, and conclusions.
- `screenshots/`: Contains screenshots supporting the activities performed.

The structure may vary depending on the type of laboratory.

---

## Results and Progress

This section will be updated as new laboratories, investigations, and practical exercises are completed.

The purpose is to maintain a transparent record of my learning progress and progressively demonstrate my skills in defensive cybersecurity and SOC operations.

---

## Legal Disclaimer

All exercises documented in this section are conducted exclusively for educational purposes and within controlled environments.

Simulation activities, threat analysis, and security testing are never performed on systems without proper authorization.

**Learn. Investigate. Detect. Defend.**

Copyright (c) 2026 Irma (Deni-0295). Todos los derechos reservados.

Este repositorio y su contenido (reportes, documentos, imágenes y textos)
son propiedad de la autora. No se permite copiar, modificar, distribuir
ni utilizar este material, total o parcialmente, sin autorización
previa y por escrito.