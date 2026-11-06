# SOC-CASE-003 — Phishing Analysis

**Mission:** 3 — Phishing Analysis  
**Analyst:** Cybersecurity Portfolio Lab  
**Status:** Investigation Documented  
**Environment:** Simulated Scenario  
**Classification:** Suspected Phishing  
**Date:** November 03, 2026

---

## 1. Executive Summary

A simulated email claiming to originate from Microsoft Security was analyzed. The message warns that the recipient's Microsoft 365 account will be suspended within 24 hours unless their identity is verified.

The email contains a suspicious sender domain, urgent language, and a URL that uses Microsoft-related terminology, although its registrable domain is `example.com`.

The provided authentication results indicate an SPF failure, no DKIM signature reported, and a DMARC failure.

**Preliminary Conclusion:** The email exhibits multiple indicators consistent with phishing. This investigation is based exclusively on simulated data and does not establish that a real security compromise occurred.

## 2. Objectives

- Identify phishing indicators in the email content.
- Analyze the sender and available email headers.
- Parse the URL and identify its registrable domain.
- Record relevant technical indicators.
- Assess potential risks to the recipient.
- Document recommended incident response actions.

## 3. Evidence Reviewed

| Evidence | Finding |
|---|---|
| Sender | `security@microsoft-support-alert.com` |
| Subject | Urgent account suspension warning |
| URL | `https://microsoft-security-verification.example.com/login` |
| Registrable domain | `example.com` |
| SPF | `fail` |
| DKIM | `none` |
| DMARC | `fail` |
| Header IP | `203.0.113.25` |

The IP address belongs to a range reserved for documentation and examples. It does not represent a verified attacker address.

## 4. Email Analysis

### 4.1 Sender Analysis

The visible sender address uses the domain `microsoft-support-alert.com`, which does not match Microsoft's official `microsoft.com` domain.

The sender name and domain may be designed to make the message appear trustworthy.

### 4.2 Social Engineering

The message uses two pressure techniques:

- **Urgency:** The recipient is instructed to act within 24 hours.
- **Threat:** The message warns that the account will be suspended.

These techniques may pressure recipients into acting without verifying the authenticity of the message.

### 4.3 URL Analysis

**Observed URL:**

`https://microsoft-security-verification.example.com/login`

- **Protocol:** HTTPS
- **Subdomain:** `microsoft-security-verification`
- **Registrable domain:** `example.com`
- **Path:** `/login`

The subdomain uses Microsoft-related terminology, but the registrable domain is not `microsoft.com`.

HTTPS protects data in transit but does not guarantee that a website is legitimate.

The `/login` path suggests that the user may be directed to a login page.

### 4.4 Email Headers and Authentication

The simulated authentication results indicate:

- **SPF: fail.** The SPF check did not pass.
- **DKIM: none.** No DKIM signature is reported in the provided results.
- **DMARC: fail.** The DMARC evaluation did not pass.
- **Return-Path:** Uses a different domain from the visible sender.

A difference between the `From` and `Return-Path` fields requires additional context and does not independently prove phishing.

## 5. Recorded Indicators

- Suspicious sender address.
- Sender domain does not match `microsoft.com`.
- URL designed to resemble a Microsoft security service.
- Registrable domain `example.com`.
- Urgent language and an account suspension threat.
- SPF and DMARC failures in the simulated data.

These findings should be assessed together. No real phishing campaign or compromised victim has been confirmed.

## 6. Risk Assessment

If a similar email were encountered in a real environment, potential risks could include:

- Credential theft.
- Unauthorized account access.
- Use of a compromised account to send additional phishing messages.
- Access to organizational resources, depending on the account's permissions.

There is no evidence in this lab that any of these impacts actually occurred.

## 7. Response Recommendations

1. Do not open the link or enter credentials.
2. Verify the message through an independent official channel.
3. Report the email to the security team.
4. In a real case, preserve the original message and its complete headers.
5. If a user submitted their credentials, follow the incident response procedure: change the credentials through a legitimate channel, revoke active sessions where appropriate, and review authentication logs.
6. In a real environment, validate indicators using authorized tools and sources before blocking domains or IP addresses.

## 8. Limitations

The scenario, email, and headers are simulated. The URL was not visited, and no external systems were contacted.

Domain reputation was not independently verified, and no threat actor attribution was attempted.

## 9. Conclusion

The simulated email exhibits multiple characteristics consistent with phishing, including apparent brand impersonation, urgency, an account suspension threat, a suspicious URL, and failed authentication results.

The available evidence supports classifying the message as **suspicious within the lab environment**.

A real investigation would require validating the information and correlating it with additional sources before reaching a definitive conclusion.