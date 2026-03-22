SELECT
    t.team_name,
    COUNT(f.incident_id) AS total_incidents,
    ROUND(AVG(f.duration_minutes), 2) AS avg_mttr_minutes
FROM {{ ref('fact_incident') }} f
JOIN {{ ref('dim_team') }} t
    ON f.team_id = t.team_id
GROUP BY t.team_name
ORDER BY avg_mttr_minutes DESC