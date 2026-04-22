# Medallion Data Platform

End-to-end data platform built on the medallion architecture (Bronze/Silver/Gold) with batch and streaming ingestion, data governance, observability, and cost optimization.

## Architecture

```
Data Sources
  ├── Batch (CSV/Parquet) ──→ Bronze Layer (raw Delta tables)
  └── Streaming (Events)  ──→ Bronze Layer (raw Delta tables)
                                    │
                                    ▼
                              Silver Layer
                              ├── Data quality checks (EXPECT constraints)
                              ├── Deduplication (window functions)
                              └── Schema validation
                                    │
                                    ▼
                              Gold Layer
                              ├── Star schema (fact + dimension tables)
                              ├── Aggregations (daily summaries, rolling avg)
                              └── BI Dashboard
                                    │
                    ┌────────────────┼────────────────┐
                    ▼                ▼                 ▼
            Unity Catalog     Observability      Cost Monitoring
            Access control    Elementary          DBU tracking
            Data lineage      Alerting            Optimization
            Audit logging     OpenLineage         Reports
                                    │
                                    ▼
                              Orchestration
                              DLT Pipeline / DAG
                              Error handling + retry
                                    │
                                    ▼
                              Testing Suite
                              Unit / integration / data quality tests
```

## Technologies

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Storage | Delta Lake, Apache Iceberg | Table formats with ACID, time travel, schema evolution |
| Compute | Apache Spark, Databricks | Batch + streaming data processing |
| Orchestration | Spark Declarative Pipelines (DLT) | Declarative pipeline orchestration |
| Quality | Great Expectations, DLT Expectations | Data validation and quarantine |
| Governance | Unity Catalog | Access control, lineage, auditing |
| Observability | Elementary, OpenLineage | Monitoring, alerting, lineage tracking |
| Visualization | Looker Studio / Tableau / Plotly | Dashboards and analytics |
| Infrastructure | Docker, Spark (local) | Local development environment |

## Project Structure

```
medallion-data-platform/
├── src/
│   ├── pipelines/          # Pipeline abstractions (batch, streaming)
│   ├── quality/            # Data validation framework
│   ├── transforms/         # Transformation strategies (sessionization, etc.)
│   ├── connectors/         # Data source factory (Delta, Iceberg, CSV)
│   ├── monitoring/         # Cost monitoring and alerting
│   └── orchestration/      # DAG execution and retry logic
├── tests/                  # Unit, integration, and data quality tests
├── notebooks/              # Databricks notebooks (exported)
├── config/                 # Pipeline and quality rule configuration
├── data/sample/            # Sample data for local testing
├── dashboards/             # Dashboard screenshots and exports
├── docs/                   # Architecture decisions, cost analysis
└── docker/                 # Local Spark + Iceberg environment
```

## Key Design Decisions

### Why Medallion Architecture?
Separating raw ingestion (Bronze), cleaning/validation (Silver), and business-level aggregation (Gold) provides clear data contracts between layers, independent testability, and the ability to replay from raw data when business logic changes.

### Why Both Delta Lake and Iceberg?
Built and benchmarked the same pipeline on both formats to understand real tradeoffs — write performance, metadata overhead, partition evolution, and ecosystem maturity. Results documented in `docs/format_comparison.md`.

### Why Star Schema for Gold Layer?
Dimensional modeling (Kimball) optimizes for analytical query patterns — wide fact tables with foreign keys to conformed dimensions. Chose star over snowflake for query simplicity at the cost of some denormalization.

## Data Quality Framework

Six quality dimensions monitored at every layer:

| Dimension | Implementation | Example |
|-----------|---------------|---------|
| **Completeness** | NOT NULL expectations | Required fields present |
| **Validity** | Format/range expectations | Email format, value bounds |
| **Uniqueness** | Deduplication with window functions | Latest record per key |
| **Consistency** | Cross-table validation | Foreign key integrity |
| **Freshness** | Timestamp-based SLA checks | Data arrives within N minutes |
| **Accuracy** | Statistical outlier detection | Values within historical range |

Invalid records are quarantined, not dropped — enabling investigation without data loss.

## How to Run

### Local Development (Spark + Docker)
```bash
cd docker/
docker-compose up -d
# Spark UI available at http://localhost:4040
```

### Databricks
Import notebooks from `notebooks/` into Databricks Free Edition workspace.

### Tests
```bash
pip install -r requirements.txt
pytest tests/ -v
```

## License

MIT
