# Architecture Diagrams

Clean, generic versions of Harish's original architecture diagrams, rebuilt from scratch as SVG (with PNG renders). Navy `#1B2A4A` + white + grey, matching the originals. All are generic clean-room recreations with synthetic data only — no company names, no locations, no proprietary details.

Rebuild them any time with `python3 build_diagrams.py` (requires `cairosvg` only for the PNG renders).

## Diagrams

### 1. `base-platform-architecture.svg`
The base platform blueprint, the standard starting point for every project: sources (APIs, SQL databases, MySQL, files, MFT, SFTP), a schema + data-quality gate that quarantines failures, the pipeline (Glue source layer → PySpark transformations → prepared tables), the Iceberg semantic layer with row/table/field filter packages, then two consumption paths — Path 1 dashboards and business users, Path 2 SQL access, REST APIs, filter packages, and downstream systems, analysts, and ML models. Platform footer: Airflow, daily DQ checks, CloudWatch, Terraform + CI/CD.
Fits in: the profile README (`harishsingi` repo).

### 2. `crm-ingestion.svg`
The redesigned CRM ingestion: the data decides, not the calendar. A CRM API (e.g. Salesforce) feeds custom Glue downloaders that read the watermark (Athena MAX(timestamp)) first, then query since that watermark; raw JSON, a schema check, then SRC → PRE → SEM (overwrite that day, upsert with full history, Iceberg-to-Iceberg promotion), consumers on SEM, a daily noon DQ check, and a self-healing banner (down 1 day or 10, the next run resumes from the watermark — no gaps, no full reloads).
Fits in: the `salesforce-crm-ingestion` repo.

### 3. `kafka-streaming-ingestion.svg`
The same base layers as diagram 1, but with streaming sources: Kafka topics, Kinesis streams, event producers, API events, CDC, and files. Stream ingestion tracks offsets and is replayable, stream processing handles late data in windows, and the footer is exactly-once / idempotent writes / replay from any offset / late data reprocessed, not lost.
Fits in: the future `kafka-streaming-ingestion` repo.

### 4. `iceberg-lakehouse.svg`
The Hive to Iceberg migration: Hive tables and metastore as the source, a staged backfill (table by table, no big-bang cutover), dual-run validation (row counts and checksums, Hive vs Iceberg side by side), cutover one table at a time with snapshot rollback, then the Iceberg target with snapshot time travel and ACID upserts, consumed by dashboards, SQL access, and ML features.
Fits in: the `hive-to-iceberg-lakehouse` repo.

### 5. `ml-demand-forecasting.svg`
ML on the gold layer: gold tables, demand history, and reference data feed feature engineering (lag demand, rolling means, seasonality by month, region mix), then training, backtesting (last 90 days held out, MAE, no leakage), and scoring (next 30 days, plain-English driver summary), consumed by dashboards, planning teams, and downstream systems, with a monitoring footer (daily DQ, forecast drift, retraining on fresh gold data).
Fits in: the `demand-forecasting-ml` repo.
