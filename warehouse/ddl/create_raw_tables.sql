CREATE TABLE IF NOT EXISTS  raw.teams(
    team_id TEXT PRIMARY KEY,
    team_name TEXT,
    org_unit TEXT,
    manager_name TEXT   
);

CREATE TABLE IF NOT EXISTS raw.services(
    service_id TEXT PRIMARY KEY,
    service_name TEXT,
    domain TEXT,
    criticality TEXT,
    owner_team_id TEXT,
    is_active BOOLEAN
);

CREATE TABLE IF NOT EXISTS raw.deployments(
    incident_id TEXT PRIMARY KEY,
    service_id TEXT,
    team_id TEXT,
    severity TEXT,
    status TEXT,
    opened_at TIMESTAMP,
    resolved_at TIMESTAMP,
    root_cause TEXT,
    customer_impact BOOLEAN,
    description TEXT
);

