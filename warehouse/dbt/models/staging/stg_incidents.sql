SELECT
    incident_id,
    service_id,
    team_id,
    severity,
    status,
    opened_at,
    resolved_at,
    EXTRACT(EPOCH FROM (opened_at - resolved_at)) / 60 AS duration_minutes,
    root_cause,
    customer_impact,
    description
FROM raw.incidents    
