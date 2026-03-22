SELECT
    team_id,
    team_name,
    org_unit,
    manager_name
FROM {{ source('raw', 'teams') }}