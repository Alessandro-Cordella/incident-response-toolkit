from fastapi import FastAPI
from datetime import datetime
from tinydb import TinyDB
import random
import uuid
import threading

app = FastAPI(
    title="Incident Response Toolkit",
    description="SOC Analyst Incident Response Simulation",
    version="1.0.0"
)

db = TinyDB("incidents.json")
incidents_table = db.table("incidents")

INCIDENT_TYPES = [
    "phishing_attempt",
    "brute_force",
    "compromised_credentials",
    "suspicious_login",
    "malware_detected",
    "privilege_escalation",
    "data_exfiltration"
]

SEVERITY_MAP = {
    "phishing_attempt": "MEDIUM",
    "brute_force": "HIGH",
    "compromised_credentials": "CRITICAL",
    "suspicious_login": "MEDIUM",
    "malware_detected": "CRITICAL",
    "privilege_escalation": "HIGH",
    "data_exfiltration": "CRITICAL"
}
PLAYBOOKS = {
    "phishing_attempt": [
        "1. Isolate the suspicious email",
        "2. Identify the sender and recipients",
        "3. Check for malicious links or attachments",
        "4. Block the sender domain",
        "5. Notify affected users",
        "6. Document and close the ticket"
    ],
    "brute_force": [
        "1. Identify the source IP",
        "2. Block the IP in the firewall",
        "3. Check if any login was successful",
        "4. Reset credentials of affected accounts",
        "5. Enable MFA if not active",
        "6. Document and close the ticket"
    ],
    "compromised_credentials": [
        "1. Immediately lock the compromised account",
        "2. Reset the password",
        "3. Review recent account activity",
        "4. Check for unauthorized access",
        "5. Notify the user and management",
        "6. Document and close the ticket"
    ],
    "suspicious_login": [
        "1. Verify the geolocation of the login",
        "2. Contact the user to confirm the access",
        "3. If unauthorized — lock the account",
        "4. Analyze access logs",
        "5. Document and close the ticket"
    ],
    "malware_detected": [
        "1. Immediately isolate the infected system",
        "2. Identify the malware type",
        "3. Run a full scan",
        "4. Remove malware or reformat the system",
        "5. Check for propagation to other systems",
        "6. Notify management",
        "7. Document and close the ticket"
    ],
    "privilege_escalation": [
        "1. Identify the account that escalated privileges",
        "2. Revoke privileges immediately",
        "3. Analyze how the escalation occurred",
        "4. Check for malicious actions taken",
        "5. Patch the exploited vulnerability",
        "6. Document and close the ticket"
    ],
    "data_exfiltration": [
        "1. Identify the exfiltrated data",
        "2. Block the exfiltration channel",
        "3. Isolate affected systems",
        "4. Assess impact and exposed data",
        "5. Notify DPO and management",
        "6. Evaluate regulatory notification obligations",
        "7. Document and close the ticket"
    ]
}
FALSE_POSITIVE_SCENARIOS = {
    "phishing_attempt": "User reported a legitimate marketing email as phishing",
    "brute_force": "Automated system running scheduled login tests",
    "compromised_credentials": "User changed password from a new device",
    "suspicious_login": "User logged in while traveling abroad",
    "malware_detected": "Antivirus false alarm on a legitimate software",
    "privilege_escalation": "IT admin performing authorized maintenance",
    "data_exfiltration": "Scheduled automated backup to cloud storage"
}

FALSE_POSITIVE_RATE = {
    "phishing_attempt": 0.4,
    "brute_force": 0.2,
    "compromised_credentials": 0.3,
    "suspicious_login": 0.5,
    "malware_detected": 0.2,
    "privilege_escalation": 0.3,
    "data_exfiltration": 0.1
}



def generate_random_incident():
    incident_type = random.choice(INCIDENT_TYPES)
    is_false_positive = random.random() < FALSE_POSITIVE_RATE[incident_type]
    
    fake_ips = ["192.168.1.10", "10.0.0.5", "172.16.0.3", "203.0.113.42", "198.51.100.7"]
    fake_users = ["john.doe", "maria.silva", "admin", "guest", "service_account"]
    fake_systems = ["WORKSTATION-01", "SERVER-DC1", "LAPTOP-HR", "SERVER-WEB", "DESKTOP-FIN"]
    
    incident = {
        "id": str(uuid.uuid4())[:8],
        "type": incident_type,
        "severity": SEVERITY_MAP[incident_type],
        "source_ip": random.choice(fake_ips),
        "affected_user": random.choice(fake_users),
        "affected_system": random.choice(fake_systems),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "OPEN",
        "is_false_positive": is_false_positive,
        "description": f"{incident_type.replace('_', ' ').title()} detected from {random.choice(fake_ips)}"
    }
    
    incidents_table.insert(incident)
    return incident



def auto_generate_incidents():
    while True:
        generate_random_incident()
        threading.Event().wait(30)



def start_auto_generation():
    thread = threading.Thread(target=auto_generate_incidents, daemon=True)
    thread.start()


from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    start_auto_generation()
    yield

app = FastAPI(
    title="Incident Response Toolkit",
    description="SOC Analyst Incident Response Simulation",
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/incidents")
def get_incidents(status: str = None, severity: str = None):
    all_incidents = incidents_table.all()
    
    if status:
        all_incidents = [i for i in all_incidents if i.get("status") == status]
    if severity:
        all_incidents = [i for i in all_incidents if i.get("severity") == severity]
    
    return {
        "total": len(all_incidents),
        "incidents": [{
            "id": i.get("id"),
            "type": i.get("type"),
            "severity": i.get("severity"),
            "source_ip": i.get("source_ip"),
            "affected_user": i.get("affected_user"),
            "affected_system": i.get("affected_system"),
            "timestamp": i.get("timestamp"),
            "status": i.get("status")
        } for i in all_incidents]
    }


@app.get("/incident/{incident_id}")
def get_incident(incident_id: str):
    all_incidents = incidents_table.all()
    incident = next((i for i in all_incidents if i.get("id") == incident_id), None)
    
    if not incident:
        return {"error": f"Incident {incident_id} not found"}
    
    return {
        "id": incident.get("id"),
        "type": incident.get("type"),
        "severity": incident.get("severity"),
        "source_ip": incident.get("source_ip"),
        "affected_user": incident.get("affected_user"),
        "affected_system": incident.get("affected_system"),
        "timestamp": incident.get("timestamp"),
        "status": incident.get("status"),
        "description": incident.get("description"),
        "playbook": PLAYBOOKS.get(incident.get("type"), [])
    }


@app.post("/investigate/{incident_id}")
def investigate_incident(incident_id: str, verdict: str, notes: str = ""):
    if verdict not in ["true_positive", "false_positive"]:
        return {"error": "Verdict must be 'true_positive' or 'false_positive'"}
    
    all_incidents = incidents_table.all()
    incident = next((i for i in all_incidents if i.get("id") == incident_id), None)
    
    if not incident:
        return {"error": f"Incident {incident_id} not found"}
    
    if incident.get("status") != "OPEN":
        return {"error": "Incident is already closed"}
    
    actual_is_fp = incident.get("is_false_positive")
    analyst_says_fp = verdict == "false_positive"
    correct = actual_is_fp == analyst_says_fp
    
    from tinydb import Query
    Q = Query()
    incidents_table.update({
        "verdict": verdict,
        "analyst_notes": notes,
        "investigated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "correct_verdict": correct
    }, Q.id == incident_id)
    
    response = {
        "incident_id": incident_id,
        "your_verdict": verdict,
        "correct": correct
    }
    
    if verdict == "false_positive":
        response["reason"] = FALSE_POSITIVE_SCENARIOS.get(incident.get("type"))
        response["message"] = "✅ Incident marked as False Positive — no action needed!" if correct else "❌ Wrong verdict! This was a real incident!"
    else:
        response["playbook"] = PLAYBOOKS.get(incident.get("type"), [])
        response["message"] = "🚨 True Positive confirmed — follow the playbook!" if correct else "❌ Wrong verdict! This was actually a False Positive!"
    
    return response




@app.post("/close/{incident_id}")
def close_incident(incident_id: str, resolution: str, actions_taken: str = ""):
    all_incidents = incidents_table.all()
    incident = next((i for i in all_incidents if i.get("id") == incident_id), None)
    
    if not incident:
        return {"error": f"Incident {incident_id} not found"}
    
    if incident.get("status") == "CLOSED":
        return {"error": "Incident is already closed"}
    
    if not incident.get("verdict"):
        return {"error": "You must investigate the incident before closing it"}
    
    from tinydb import Query
    Q = Query()
    incidents_table.update({
        "status": "CLOSED",
        "resolution": resolution,
        "actions_taken": actions_taken,
        "closed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }, Q.id == incident_id)
    
    return {
        "incident_id": incident_id,
        "status": "CLOSED",
        "type": incident.get("type"),
        "severity": incident.get("severity"),
        "verdict": incident.get("verdict"),
        "resolution": resolution,
        "actions_taken": actions_taken,
        "opened_at": incident.get("timestamp"),
        "closed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "message": "✅ Incident closed successfully and documented!"
    }



@app.get("/dashboard")
def get_dashboard():
    all_incidents = incidents_table.all()
    
    open_incidents = [i for i in all_incidents if i.get("status") == "OPEN"]
    closed_incidents = [i for i in all_incidents if i.get("status") == "CLOSED"]
    
    by_severity = {}
    for incident in all_incidents:
        severity = incident.get("severity")
        if severity in by_severity:
            by_severity[severity] += 1
        else:
            by_severity[severity] = 1
    
    by_type = {}
    for incident in all_incidents:
        itype = incident.get("type")
        if itype in by_type:
            by_type[itype] += 1
        else:
            by_type[itype] = 1
    
    correct_verdicts = [i for i in closed_incidents if i.get("correct_verdict") == True]
    wrong_verdicts = [i for i in closed_incidents if i.get("correct_verdict") == False]
    
    accuracy = 0
    if closed_incidents:
        accuracy = round(len(correct_verdicts) / len(closed_incidents) * 100, 1)
    
    critical_open = [i for i in open_incidents if i.get("severity") == "CRITICAL"]
    
    return {
        "total_incidents": len(all_incidents),
        "open_incidents": len(open_incidents),
        "closed_incidents": len(closed_incidents),
        "by_severity": by_severity,
        "by_type": by_type,
        "analyst_accuracy": f"{accuracy}%",
        "correct_verdicts": len(correct_verdicts),
        "wrong_verdicts": len(wrong_verdicts),
        "critical_open": len(critical_open),
        "critical_open_detail": critical_open
    }


@app.get("/report")
def get_report():
    all_incidents = incidents_table.all()
    closed_incidents = [i for i in all_incidents if i.get("status") == "CLOSED"]
    open_incidents = [i for i in all_incidents if i.get("status") == "OPEN"]
    
    true_positives = [i for i in closed_incidents if i.get("verdict") == "true_positive"]
    false_positives = [i for i in closed_incidents if i.get("verdict") == "false_positive"]
    
    correct_verdicts = [i for i in closed_incidents if i.get("correct_verdict") == True]
    accuracy = 0
    if closed_incidents:
        accuracy = round(len(correct_verdicts) / len(closed_incidents) * 100, 1)
    
    most_common_type = None
    type_counts = {}
    for incident in all_incidents:
        itype = incident.get("type")
        if itype in type_counts:
            type_counts[itype] += 1
        else:
            type_counts[itype] = 1
    if type_counts:
        most_common_type = max(type_counts, key=type_counts.get)
    
    critical_unresolved = [i for i in open_incidents if i.get("severity") == "CRITICAL"]
    
    return {
        "report_generated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "summary": {
            "total_incidents": len(all_incidents),
            "open_incidents": len(open_incidents),
            "closed_incidents": len(closed_incidents),
            "true_positives": len(true_positives),
            "false_positives": len(false_positives),
            "analyst_accuracy": f"{accuracy}%",
            "most_common_incident_type": most_common_type
        },
        "critical_unresolved": critical_unresolved,
        "recommendations": [
            "Prioritize CRITICAL incidents immediately",
            "Review false positive patterns to improve detection rules",
            "Ensure all incidents are investigated within SLA",
            "Document all actions taken for audit trail"
        ]
    }