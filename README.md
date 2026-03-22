# OpsPulse: Incident Intelligence Data Platform

## Overview
End-to-end data engineering pipeline for incident analytics.

This project simulates a real-world data platform that ingests operational incident data, transforms it using dbt, and builds structured warehouse tables.

## Architecture
Raw → Staging → Core

## Stack
- Python (ingestion)
- PostgreSQL (Docker)
- dbt (transformations)
- SQL

## Features
- Synthetic incident data generation
- Raw ingestion pipeline
- dbt staging models
- Core warehouse tables (fact + dimensions)

## Next Steps
- Analytics marts (MTTR, incident trends)
- Airflow orchestration
- Data quality tests
