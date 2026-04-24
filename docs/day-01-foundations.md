# Day 1 — Foundations: Spark + Delta Lake

**Date:** 2026-04-23 → 2026-04-24

## Goal

Stand up the project's foundational abstractions — a reusable SparkSession
configured for Delta Lake, and a Bronze layer ingestion module that reads raw
delivery events into a Delta table. Everything downstream (Silver, Gold,
streaming, quality, orchestration) builds on this.

## What was built

| Component | Location | Purpose |
|-----------|----------|---------|
| SparkSession factory | `src/spark/session.py` | Single source of truth for Spark + Delta configuration. Prevents config drift between pipelines. |
| Bronze ingestion | `src/pipelines/bronze/ingest_delivery_events.py` | Reads source JSON, writes a Delta table with no transformation. |
| CLI entry point | `scripts/run_bronze_ingest.py` | Runnable demo that wires the two together against sample data. |
| Sample data | `data/sample/delivery_events.json` | Five delivery events covering delivered, cancelled, and in-transit statuses. |
| Tests | `tests/test_spark_session.py` | Smoke tests verifying Delta catalog and extensions are active. |

## Design decisions

### Why centralize SparkSession config

Every pipeline (Bronze, Silver, Gold) needs the same Delta Lake configuration:
`DeltaCatalog` on `spark_catalog`, `DeltaSparkSessionExtension` on
`spark.sql.extensions`, and the Delta JARs on the classpath. If each pipeline
builds its own session, small config drift breaks things invisibly. One factory,
one config.

### Why JSON for sample data

The Bronze layer is "data as it arrived" — JSON is the common format for event
streams (Kafka, Kinesis, webhooks). Using JSON here makes the Bronze read path
realistic. Parquet would be wrong — Parquet is a destination format, not a
source format.

### Why `overwrite` mode for now

Day 1's ingestion is a full refresh — the sample data is small and the pipeline
is idempotent. Day 2 switches to append + schema evolution for real incremental
ingestion.

## How to run

```bash
# From repo root
pip install -r requirements.txt
python scripts/run_bronze_ingest.py
```

Expected: five rows written to `/tmp/medallion-bronze/delivery_events`, schema
printed, and the DataFrame displayed.

```bash
# Run tests
pytest tests/ -v
```

## What's next (Day 2)

- Define an explicit schema for Bronze instead of relying on inference
- Handle schema evolution (new columns appearing in future events)
- Partition the Bronze table by event date for query efficiency
- Add a Silver layer skeleton for deduplication + quality checks
