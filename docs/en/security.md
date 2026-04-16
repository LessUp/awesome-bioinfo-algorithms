---
title: Security Policy
layout: default
nav_order: 7
description: "Vulnerability reporting and handling process"
---

# Security Policy
{: .no_toc }

This document outlines security procedures and general policies for the Awesome Bioinformatics Algorithms project.
{: .fs-6 .fw-300 }

<details open markdown="block">
  <summary>Table of Contents</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## Supported Versions

We release patches for security vulnerabilities. Which versions are eligible?

| Version | Supported |
|:--------|:----------|
| 1.0.x   | ✅ Yes    |
| < 1.0   | ❌ No     |

Always use the latest version to ensure you receive security updates.

---

## Reporting a Vulnerability

{: .warning }
**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via:

### Email
Send an email to: **security@lessup.org**

### GitHub Security Advisory
1. Go to the repository Security tab
2. Click "Report a vulnerability"
3. Fill out the vulnerability report form

### What to Include

Your report should include:

1. **Description** — Clear description of the vulnerability
2. **Impact** — What can be exploited and potential impact
3. **Reproduction Steps** — Step-by-step instructions to reproduce
4. **Affected Versions** — Which versions are affected
5. **Suggested Fix** — (Optional) Your recommendations for fixing

---

## Response Process

When we receive a security report, we follow this process:

| Phase | Timeline | Actions |
|:------|:---------|:--------|
| Acknowledgment | Within 48 hours | Confirm receipt of report |
| Assessment | 1 week | Evaluate severity and impact |
| Patch Development | Varies by severity | Develop and test fix |
| Disclosure | After fix release | Publish security advisory |

### Communication

- We will keep you informed of our progress
- We may ask for additional information if needed
- You will be credited in the security advisory (unless you prefer anonymity)

---

## Disclosure Policy

When we receive a security bug report, we will:

1. Confirm the issue and determine affected versions
2. Audit code to find any similar problems
3. Prepare fixes for all supported versions
4. Release new versions as soon as possible
5. Publish a security advisory on GitHub

---

## Security Best Practices

### For Users

- Always use the latest version
- Validate algorithm data with `python -m scripts validate`
- Don't modify data files manually without validation
- Use virtual environments for development

### For Contributors

- Never commit secrets or credentials
- Validate all inputs when adding new algorithms
- Follow the YAML schema strictly
- Run validation before submitting PRs

---

## Past Security Advisories

No security advisories have been issued for this project to date.

---

## Scope

### In Scope

- Python code in `scripts/`
- Data validation logic
- CLI tool security
- Documentation security

### Out of Scope

- Third-party dependencies (report to their maintainers)
- Algorithm implementations we link to
- GitHub infrastructure (report to GitHub)

---

## Questions?

If you have questions about this security policy, please:

- Email: security@lessup.org
- Open a non-sensitive issue on GitHub

Thank you for helping keep Awesome Bioinformatics Algorithms secure!
