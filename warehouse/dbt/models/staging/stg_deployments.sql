SELECT
    deployment_id,
    service_id,
    deployed_at,
    release_verson,
    deployment_status,
    rollback_flag
FROM raw.deployments
