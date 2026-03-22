SELECT
    deployment_id,
    service_id,
    deployed_at::timestamp AS deployed_at,
    release_version,
    deployment_status,
    rollback_flag
FROM {{ source('raw', 'deployments') }}