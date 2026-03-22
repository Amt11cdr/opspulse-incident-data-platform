# OpsPulse: Incident Intelligence Data Platform

## Overview

OpsPulse is an end-to-end data engineering pipeline that simulates a real-world incident analytics platform.

It ingests operational data, transforms it using dbt, and builds structured warehouse models for reliability analysis.

## Architecture

```
Raw (CSV ingestion)
   ↓
Postgres (raw schema)
   ↓
dbt staging models
   ↓
core warehouse tables (fact + dimensions)
```

## Tech Stack

* Python (data generation + ingestion)
* PostgreSQL (Docker)
* dbt (transformations)
* SQL

## Key Features

* Synthetic incident data pipeline
* Layered warehouse design (raw → staging → core)
* dbt-based transformation logic
* Fact and dimension modeling

## Example Analytics

* Incident duration calculation (MTTR)
* Service-level incident tracking

## Project Structure

```
ingestion/
warehouse/
opspulse_dbt/
```

## Next Steps

* Add analytics marts (MTTR, trends)
* Add Airflow orchestration
* Add data quality tests
