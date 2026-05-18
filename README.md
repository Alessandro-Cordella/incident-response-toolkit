# Incident Response Toolkit

A SOC Analyst simulation built with Python and FastAPI that automatically generates security incidents and guides the analyst through the full incident response lifecycle.

## Features
- Automatic incident generation every 30 seconds
- 7 incident types with realistic false positive rates
- Built-in playbooks for each incident type
- Triage system — true positive vs false positive
- Full incident lifecycle — Open, Investigate, Close
- Analyst accuracy tracking
- Security report generation
- Fully containerized with Docker

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

## Endpoints
| Method | Endpoint | Description |
|---|---|---|
| GET | /incidents | List all incidents |
| GET | /incident/{id} | Get incident details + playbook |
| POST | /investigate/{id} | Submit verdict — true/false positive |
| POST | /close/{id} | Close incident with resolution |
| GET | /dashboard | Analyst statistics and accuracy |
| GET | /report | Full security report |

## Tech Stack
- Python 3.11
- FastAPI
- TinyDB
- Docker

## How to run
```bash
docker build -t incident-response .
docker run -p 8000:8000 incident-response
```

## Known Limitations
- Incident data is simulated — not connected to real log sources
- No authentication
- TinyDB not suitable for production scale
