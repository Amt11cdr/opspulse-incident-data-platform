SELECT
    i.incident_id,
    i.service_id,
    i.team_id,
    i.severity,
    i.status,
    i.opened_at,
    i.resolved_at,
    i.duration_minutes,
    i.root_cause,
    i.customer_impact
FROM {{ ref('stg_incidents') }} i