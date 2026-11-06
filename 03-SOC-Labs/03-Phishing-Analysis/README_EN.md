[Versión español](README.md)

# Laboratory 3 — Phishing Analysis

## Description

A practical cybersecurity lab focused on suspicious email analysis, phishing indicator identification, and investigation documentation using a SOC analyst approach.

The scenario simulates an email impersonating Microsoft Security and pressuring the recipient to verify their account through a login link.

**Important:** All scenario data is fictional. This activity is intended for educational purposes only.

## Objectives

- Identify social engineering techniques.
- Analyze the sender and available email headers.
- Interpret SPF, DKIM, and DMARC authentication results.
- Parse a URL and identify its registrable domain.
- Record technical indicators and phishing signals.
- Assess potential credential theft risks.
- Document findings and incident response recommendations.

## Lab Structure

```text
03-Phishing-Analysis/
├── README.md
├── README_EN.md
├── evidence/
│   ├── email-header.txt
│   ├── indicators.txt
│   ├── urls.txt
│   └── analysis-notes.txt
├── investigation.md
├── investigation_EN.md
└── screenshots/
```

## Evidence

| File | Description |
|---|---|
| `email-header.txt` | Simulated email headers and authentication results. |
| `indicators.txt` | Technical indicators and identified phishing signals. |
| `urls.txt` | URL structure and domain analysis. |
| `analysis-notes.txt` | Technical notes, potential risks, and preliminary conclusions. |
| `investigation.md` | Complete investigation report in Spanish. |
| `investigation_EN.md` | Complete investigation report in English. |

## Main Findings

- Sender domain differs from `microsoft.com`.
- Urgent language and an account suspension threat.
- A URL containing a Microsoft-related subdomain.
- Registrable domain identified as `example.com`.
- SPF and DMARC failures in the simulated data.
- Potential credential harvesting risk.

## Tools and Concepts

- Manual email analysis.
- Email header analysis.
- URL analysis.
- IOC (Indicator of Compromise) identification.
- SPF, DKIM, and DMARC.
- Social engineering.
- Incident investigation and documentation.

## Conclusion

The simulated scenario presents multiple characteristics consistent with phishing. The findings support classifying the email as suspicious within the lab environment, but they do not establish that a real attack or security compromise occurred.

## Disclaimer

This lab uses simulated data exclusively. No suspicious URL was opened, no external systems were contacted, and no real threat actor attribution was attempted.