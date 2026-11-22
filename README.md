# Harish Reddy Singi Reddy

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=2F81F7&center=true&vCenter=true&width=500&lines=Senior+Data+Engineer;Python+%E2%80%A2+SQL+%E2%80%A2+PySpark+%E2%80%A2+AWS;Lakehouses+%E2%80%A2+ETL+%E2%80%A2+ML+on+data)](https://git.io/typing-svg)

[![Senior Data Engineer](https://img.shields.io/badge/Senior%20Data%20Engineer-7%2B%20yrs-blue?style=for-the-badge)](https://github.com/harishsingi)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://github.com/harishsingi)
[![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)](https://github.com/harishsingi)
[![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white)](https://github.com/harishsingi)
[![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white)](https://github.com/harishsingi)

> I build data pipelines that business teams can trust: governed, quality-checked, and tied to a clear outcome.

<details>
<summary><b>About me</b></summary>

<br>

Senior Data Engineer with 7+ years building production data pipelines, lakehouses, and analytics platforms.

- End-to-end ownership: ingestion, transformation, orchestration, quality checks, and the analytics layer on top
- I care about the boring parts that make data usable: contracts, tests, monitoring, and on-call ownership
- I mentor junior data engineers and I like turning messy, real-world data into something a team can decide on

</details>

<details>
<summary><b>What I do best</b></summary>

<br>

| Area | What that means in practice |
|---|---|
| Lakehouses | Hive to Apache Iceberg migrations, snapshot time travel, Spark at petabyte scale |
| Pipelines | PySpark, Airflow, AWS Glue, EMR, Lambda, S3, Athena, Kafka, Kinesis |
| Modelling | Dimensional modelling, SCD Type 1/2, dbt, Trino, governed gold layers |
| ML on data | Demand forecasting, fraud and risk scoring, BERT classification for customer topics |
| Platform | Terraform, Docker, GitHub Actions CI/CD, CloudWatch, data quality frameworks |

</details>

## 📊 GitHub stats

![Harish's GitHub stats](https://github-readme-stats.vercel.app/api?username=harishsingi&show_icons=true&theme=default&hide_border=true&count_private=true)
![Top languages](https://github-readme-stats.vercel.app/api/top-langs/?username=harishsingi&layout=compact&theme=default&hide_border=true&count_private=true)

## 🛠️ Stack at a glance

[![My Skills](https://skillicons.dev/icons?i=python,aws,apachekafka,terraform,docker,git,githubactions,snowflake,postgres,mysql,linux&theme=light)](https://skillicons.dev)

## 🧭 How a pipeline I build looks

This is my base platform architecture, the standard blueprint every project starts from, covering all sources and both consumption paths, unless a pipeline needs a specific change.

**Interactive version:** [Explore the architectures live](https://harishsingi.github.io/harishsingi/architecture-explorer/) — click any service to see what it does, and send a record through the pipeline.

![Base platform architecture](docs/architecture/base-platform-architecture.svg)

```mermaid
flowchart LR
    A[Sources<br/>APIs, files, events, CRM] --> B[Ingestion<br/>Glue / Kafka / Kinesis]
    B --> C[Bronze<br/>Raw, immutable]
    C --> D[Silver<br/>Cleaned, validated, DQ checks]
    D --> E[Gold<br/>Dimensional, SCD 1/2]
    E --> F[BI dashboards<br/>QuickSight / Power BI]
    E --> G[ML features<br/>Forecasting / risk scoring]
    D -.-> H[Alerts<br/>CloudWatch, on-call]
```

<details>
<summary><b>🏗️ Base architecture, step by step</b></summary>

<br>

1. **Ingest:** Glue downloaders, Kafka, or Kinesis land data raw and immutable, per source.
2. **Bronze:** raw JSON or files, schema checked on the way in.
3. **Silver:** cleaned and validated, duplicates removed, quality checks before anything moves on.
4. **Gold:** dimensionally modelled, SCD Type 1/2, governed with access controls.
5. **Consume:** the same gold layer feeds BI dashboards and ML features, so the two never drift apart.
6. **Operate:** daily DQ checks on the latest timestamp, alerts if no new data, on-call ownership.

</details>

## 📈 Activity

![Harish's activity graph](https://github-readme-activity-graph.vercel.app/graph?username=harishsingi&theme=github-compact&hide_border=true)

<details>
<summary><b>🔍 Project deep dives, click to open</b></summary>

<br>

- **AWS pipeline starter kit:** Glue job, Lambda validator, Athena queries, Terraform for the whole stack, data quality checks before anything lands in gold.
- **Iceberg lakehouse:** Hive tables migrated to Iceberg, snapshot time travel to roll back a bad load, Airflow orchestrating the migration in stages.
- **Demand forecasting:** lag and rolling features, seasonal patterns, backtest on the last 90 days with no leakage, plain-English driver summary per product.
- **Credit fraud risk:** feature store style inputs, a transparent scoring model, and a score entry point you can run on a single record.
- **People analytics:** lifecycle data into governed layers, row and column level access controls, attrition and headcount reporting.
- **Incentive analytics:** heavy Snowflake transformations, tiering by historic patterns, dashboard-ready gold table.
- **Salesforce CRM ingestion:** Glue downloaders, SRC overwrites that day, PRE upserts with dedupe on record Id, SEM applies deletes via is_deleted, and a target-timestamp catch-up that self-heals after outages.

</details>

<details>
<summary><b>💬 Ask me about</b></summary>

<br>

- Lakehouse migrations, Hive to Iceberg, and when not to migrate
- Data quality that actually catches bad loads before dashboards do
- Dimensional modelling, SCD Type 1/2, and gold layer design
- PySpark performance tuning and Airflow orchestration
- Demand forecasting and fraud scoring on real, messy data

</details>

## Featured projects

Click a project to explore it. Every repo runs locally with synthetic data, no setup beyond Python.

| Project | Try it | What it demonstrates |
|---|---|---|
| [aws-data-pipeline-starter-kit](https://github.com/harishsingi/aws-data-pipeline-starter-kit) | `make demo` | Production-grade AWS pipeline: Glue, EMR, Lambda, S3, Athena, Terraform, Docker, data quality |
| [hive-to-iceberg-lakehouse](https://github.com/harishsingi/hive-to-iceberg-lakehouse) | `python -m src.migrate` | Lakehouse migration, snapshot time travel, Spark, Airflow orchestration |
| [demand-forecasting-ml](https://github.com/harishsingi/demand-forecasting-ml) | `python -m src.score` | ML demand forecasting: feature engineering, backtesting, plain-English driver summary |
| [credit-fraud-risk-model](https://github.com/harishsingi/credit-fraud-risk-model) | `python -m src.score` | Fraud and risk scoring for credit eligibility decisions |
| [people-analytics-warehouse](https://github.com/harishsingi/people-analytics-warehouse) | `python -m src.build` | Governed HR warehouse: lifecycle data, SCD 1/2, attrition and headcount reporting, access controls |
| [incentive-analytics-snowflake](https://github.com/harishsingi/incentive-analytics-snowflake) | `python -m src.build_gold` | Snowflake-style transformations for incentive dashboards, invoice and cost reporting |
| [salesforce-crm-ingestion](https://github.com/harishsingi/salesforce-crm-ingestion) | `python -m src.src_to_pre` | Salesforce CRM ingestion: SRC/PRE/SEM, dedupe on record Id, deletes via is_deleted, self-healing incremental loads |

> These repos are clean-room portfolio recreations of production work. All data is synthetic, and no proprietary code, data, schema names, or internal system details from any employer are included.

<details>
<summary><b>Core stack</b></summary>

<br>

- **Languages:** Python, SQL, PySpark, C
- **AWS:** Glue, EMR, Lambda, S3, Athena, CloudWatch, Step Functions
- **Data platform:** Apache Iceberg, Apache Spark, Airflow, Databricks, Snowflake, dbt, Trino, Kafka, Kinesis
- **Engineering:** Terraform, Docker, GitHub Actions CI/CD, Git, data quality frameworks, dimensional modelling (SCD Type 1/2)
- **BI and ML:** QuickSight, Power BI, demand forecasting, fraud and risk models, BERT classification

</details>

<details>
<summary><b>Education</b></summary>

<br>

- MS, Business Analytics, concentration in Data Engineering and Infrastructure
- Bachelor's, Computer Science

</details>

## Get in touch

- Email: sharishreddy.2023@gmail.com
- Open to relocate anywhere in the USA
- 🌱 Currently exploring: streaming ingestion, data observability, and agentic data infrastructure
