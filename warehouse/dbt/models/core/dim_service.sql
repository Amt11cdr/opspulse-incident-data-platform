SELECT
    service_id,
    service_name,
    domain,
    criticality,
    owner_team_id,
FROM {{ ref('stg_services') }}    
