# Incident Response Toolkit

A SOC Analyst simulation platform built with Python and FastAPI that automatically generates security incidents and guides analysts through the complete incident response lifecycle.

---

## Features

- Automatic incident generation every 30 seconds
- 7 different incident types
- Realistic false positive simulation
- Built-in incident response playbooks
- Analyst investigation workflow
- True Positive vs False Positive classification
- Full incident lifecycle management
- Analyst accuracy tracking
- Dashboard and reporting system
- Docker support

---

## Incident Types

| Incident Type | Severity | False Positive Rate |
|---|---|---|
| MALWARE_DETECTED | CRITICAL | 20% |
| COMPROMISED_CREDENTIALS | CRITICAL | 30% |
| DATA_EXFILTRATION | CRITICAL | 10% |
| PRIVILEGE_ESCALATION | HIGH | 30% |
| BRUTE_FORCE | HIGH | 20% |
| PHISHING_ATTEMPT | MEDIUM | 40% |
| SUSPICIOUS_LOGIN | MEDIUM | 50% |

---

## Example Incident

```json
{
  "id": "f81c2a9b",
  "type": "BRUTE_FORCE",
  "severity": "HIGH",
  "source_ip": "203.0.113.42",
  "affected_user": "admin",
  "affected_system": "SERVER-WEB",
  "timestamp": "2025-09-22 10:45:12",
  "status": "OPEN"
}
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /incidents | List all incidents |
| GET | /incident/{id} | Get incident details and playbook |
| POST | /investigate/{id} | Submit analyst verdict |
| POST | /close/{id} | Close an incident |
| GET | /dashboard | Analyst metrics and statistics |
| GET | /report | Generate security report |

---

## Architecture

FASTAPI APPLICATION
↓
INCIDENT GENERATOR
↓
TINYDB STORAGE
↓
DASHBOARD / REPORTS / INVESTIGATION WORKFLOW

---

## Tech Stack

- Python 3.11
- FastAPI
- TinyDB
- Docker

---

## Running the Project

Local Setup

Docker Setup
API Documentation available at http://localhost:8000/docs

---

## Known Limitations

- Incident data is fully simulated
- No real SIEM or log ingestion integration
- No authentication or RBAC
- TinyDB is not suitable for production-scale environments
- Background incident generation uses threading and is intended for demo purposes

---

## Future Improvements

- JWT authentication
- Role-based access control
- PostgreSQL integration
- Real SIEM log ingestion
- WebSocket live incident updates
- Analyst leaderboard
- MITRE ATT&CK mapping
- Email alerting system
- Incident escalation workflow

---

## Disclaimer

This project is intended for educational and portfolio purposes only. It simulates SOC workflows and does not replace a real SIEM or enterprise incident response platform.
