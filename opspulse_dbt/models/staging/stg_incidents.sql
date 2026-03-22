SELECT
    incident_id,
    service_id,
    team_id,
    severity,
    status,
    opened_at::timestamp AS opened_at,
    resolved_at::timestamp AS resolved_at,
    EXTRACT(EPOCH FROM (
        resolved_at::timestamp - opened_at::timestamp
    )) / 60 AS duration_minutes,
    root_cause,
    customer_impact,
    description
FROM {{ source('raw', 'incidents') }}