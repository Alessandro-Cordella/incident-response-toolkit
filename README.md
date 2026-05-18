# Incident Response Toolkit

A SOC Analyst simulation built with Python and FastAPI that automatically generates security incidents and guides analysts through the full incident response lifecycle.

---

## Features

- Automatic incident generation every 30 seconds
- 7 incident types with realistic false positive rates
- Built-in response playbooks
- Triage workflow (True Positive vs False Positive)
- Full incident lifecycle management
- Analyst accuracy tracking
- Security reporting dashboard
- Docker support

---

## Incident Types

| Type | Severity | False Positive Rate |
|---|---|---|
| malware_detected | CRITICAL | 20% |
| compromised_credentials | CRITICAL | 30% |
| data_exfiltration | CRITICAL | 10% |
| privilege_escalation | HIGH | 30% |
| brute_force | HIGH | 20% |
| phishing_attempt | MEDIUM | 40% |
| suspicious_login | MEDIUM | 50% |

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/incidents` | List all incidents |
| GET | `/incident/{id}` | Get incident details and playbook |
| POST | `/investigate/{id}` | Submit analyst verdict |
| POST | `/close/{id}` | Close an incident |
| GET | `/dashboard` | Analyst metrics and statistics |
| GET | `/report` | Generate security report |

---

## Architecture

```text
FastAPI Application
        ↓
Incident Generator
        ↓
TinyDB Storage
        ↓
Dashboard / Reports / Investigation Workflow
