# Incident Response Toolkit
A SOC Analyst incident response simulation built with Python and FastAPI.
This project simulates the workflow of a Security Operations Center (SOC) analyst by generating security incidents, allowing investigation and triage, and tracking analyst decisions throughout the incident lifecycle.
## Purpose
The goal of this project is to practice and demonstrate:
- Incident triage workflows
- False positive analysis
- Security incident handling
- Basic SOC operations
- REST API development with FastAPI
- Security-oriented backend design
## Features
- Automatic incident generation every 30 seconds
- Multiple security incident categories
- Configurable false positive rates
- Built-in incident response playbooks
- Incident investigation workflow
- True positive vs false positive classification
- Incident closure and resolution tracking
- Analyst accuracy metrics
- Dashboard and reporting endpoints
- Docker support
---
# Incident Types
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
# Example Incident
```json
{
  "id": "a1b2c3d4",
  "type": "brute_force",
  "severity": "HIGH",
  "source_ip": "203.0.113.42",
  "affected_user": "admin",
  "affected_system": "SERVER-WEB",
  "timestamp": "2025-09-22 10:45:12",
  "status": "OPEN"
}
API Endpoints
Method    Endpoint    Description
GET    /incidents    List incidents
GET    /incident/{id}    Get incident details and playbook
POST    /investigate/{id}    Submit analyst verdict
POST    /close/{id}    Close an incident
GET    /dashboard    Analyst metrics and statistics
GET    /report    Generate security report
Architecture
FastAPI Application
        ↓
Incident Generator
        ↓
TinyDB Storage
        ↓
Dashboard / Reports / Investigation Workflow
Tech Stack
Python 3.11
FastAPI
TinyDB
Docker
Running the Project
Local
pip install -r requirements.txt
uvicorn main:app --reload
Docker
docker build -t incident-response .
docker run -p 8000:8000 incident-response
API documentation available at:
http://localhost:8000/docs
Known Limitations
Incident data is fully simulated
No real SIEM or log ingestion integration
No authentication or RBAC
TinyDB is not suitable for production-scale environments
Background incident generation uses threading and is intended for demo purposes
