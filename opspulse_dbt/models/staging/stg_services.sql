SELECT
    service_id,
    service_name,
    LOWER(domain) AS domain,
    LOWER(criticality) AS criticality,
    owner_team_id,
    is_active
FROM {{ source('raw', 'services') }}