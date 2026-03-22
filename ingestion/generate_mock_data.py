import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta
import random

BASE_PATH = "data/raw"

os.makedirs(f"{BASE_PATH}/teams", exist_ok=True)
os.makedirs(f"{BASE_PATH}/services", exist_ok=True)
os.makedirs(f"{BASE_PATH}/incidents", exist_ok=True)
os.makedirs(f"{BASE_PATH}/deployments", exist_ok=True)


# --------------------
# TEAMS
# --------------------
teams = []

team_names = [
    "Payments Platform",
    "Auth Systems",
    "Checkout Experience",
    "Search Infrastructure",
    "Notifications",
    "Customer Data",
    "Observability",
    "Recommendations"
]

for i, name in enumerate(team_names):
    teams.append({
        "team_id": f"T{i+1}",
        "team_name": name,
        "org_unit": "Engineering",
        "manager_name": f"Manager_{i+1}"
    })

teams_df = pd.DataFrame(teams)
teams_df.to_csv(f"{BASE_PATH}/teams/teams.csv", index=False)


# --------------------
# SERVICES
# --------------------
services = []

service_names = [
    "payment-api",
    "fraud-service",
    "auth-service",
    "user-session",
    "checkout-api",
    "search-api",
    "email-service",
    "push-service",
    "customer-profile",
    "event-processor",
    "metrics-collector",
    "recommendation-engine"
]

for i, name in enumerate(service_names):
    services.append({
        "service_id": f"S{i+1}",
        "service_name": name,
        "domain": random.choice(["payments", "identity", "commerce", "infra"]),
        "criticality": random.choice(["low", "medium", "high"]),
        "owner_team_id": random.choice(teams_df["team_id"]),
        "is_active": True
    })

services_df = pd.DataFrame(services)
services_df.to_csv(f"{BASE_PATH}/services/services.csv", index=False)


# --------------------
# DEPLOYMENTS
# --------------------
deployments = []

start_date = datetime(2024, 1, 1)

for i in range(600):

    deployed_at = start_date + timedelta(days=random.randint(0, 300))

    deployments.append({
        "deployment_id": f"D{i+1}",
        "service_id": random.choice(services_df["service_id"]),
        "deployed_at": deployed_at,
        "release_version": f"v{random.randint(1,5)}.{random.randint(0,20)}",
        "deployment_status": random.choice(["success", "success", "success", "failed"]),
        "rollback_flag": random.choice([True, False, False])
    })

deployments_df = pd.DataFrame(deployments)
deployments_df.to_csv(f"{BASE_PATH}/deployments/deployments.csv", index=False)


# --------------------
# INCIDENTS
# --------------------
incidents = []

severities = ["SEV1", "SEV2", "SEV3", "SEV4"]

for i in range(400):

    opened = start_date + timedelta(days=random.randint(0, 300))
    duration_minutes = random.randint(10, 240)

    resolved = opened + timedelta(minutes=duration_minutes)

    service = services_df.sample(1).iloc[0]

    incidents.append({
        "incident_id": f"I{i+1}",
        "service_id": service["service_id"],
        "team_id": service["owner_team_id"],
        "severity": random.choices(
            severities,
            weights=[5, 15, 40, 40]
        )[0],
        "status": "resolved",
        "opened_at": opened,
        "resolved_at": resolved,
        "root_cause": random.choice([
            "deployment_bug",
            "infrastructure",
            "configuration",
            "dependency_failure"
        ]),
        "customer_impact": random.choice([True, False]),
        "description": "Auto-generated incident"
    })

incidents_df = pd.DataFrame(incidents)
incidents_df.to_csv(f"{BASE_PATH}/incidents/incidents.csv", index=False)


print("Mock data generated successfully.")
