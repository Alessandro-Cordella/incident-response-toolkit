Incident Response Toolkit

A SOC Analyst incident response simulation built with Python and FastAPI.
The application automatically generates security incidents and allows analysts to investigate, classify, and close them through a realistic incident response workflow.

Features
Automatic incident generation every 30 seconds
Multiple realistic security incident types
Configurable false positive simulation
Built-in response playbooks for each incident type
Incident triage workflow
True positive vs false positive classification
Incident lifecycle management
Analyst performance and accuracy tracking
Dashboard and reporting endpoints
Docker support for easy deployment
Incident Types
Incident Type	Severity	False Positive Rate
malware_detected	CRITICAL	20%
compromised_credentials	CRITICAL	30%
data_exfiltration	CRITICAL	10%
privilege_escalation	HIGH	30%
brute_force	HIGH	20%
phishing_attempt	MEDIUM	40%
suspicious_login	MEDIUM	50%
Example Incident
{
  "id": "7c1f92ab",
  "type": "brute_force",
  "severity": "HIGH",
  "source_ip": "203.0.113.42",
  "affected_user": "admin",
  "affected_system": "SERVER-WEB",
  "timestamp": "2025-09-22 10:45:12",
  "status": "OPEN"
}
API Endpoints
Method	Endpoint	Description
GET	/incidents	List all incidents
GET	/incident/{id}	Get incident details and response playbook
POST	/investigate/{id}	Submit analyst verdict
POST	/close/{id}	Close an incident
GET	/dashboard	Analyst metrics and statistics
GET	/report	Generate security report
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
Local Setup
pip install -r requirements.txt
uvicorn main:app --reload

The API documentation will be available at:

http://localhost:8000/docs
Docker Setup
docker build -t incident-response .
docker run -p 8000:8000 incident-response
Known Limitations
Incident data is fully simulated
No real SIEM or log ingestion integration
No authentication or RBAC
TinyDB is not suitable for production-scale environments
Background incident generation uses threading and is intended for demo purposes
Purpose of the Project

This project was designed as a practical SOC analyst training environment to simulate real-world incident handling workflows, including:

Incident triage
Investigation processes
Analyst decision-making
False positive handling
Reporting and documentation

It is intended for
