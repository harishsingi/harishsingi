#!/usr/bin/env python3
"""Build 5 clean, generic architecture diagrams as SVG.
Theme: navy #1B2A4A + white + grey, matching Harish's originals.
No company names, no locations, no proprietary details.
Run: python3 build_diagrams.py  -> writes *.svg next to this script.
"""
import os
from xml.sax.saxutils import escape

OUT = os.path.dirname(os.path.abspath(__file__))
NAVY = "#1B2A4A"
NAVY2 = "#24365E"
GREY = "#3D3D3D"
LIGHT = "#F4F6F9"
BORDER = "#1B2A4A"
SUB = "#555555"
W = 1200

DEFS = """<defs>
<marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#1B2A4A"/></marker>
<marker id="arrW" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#FFFFFF"/></marker>
</defs>"""

def esc(s):
    return escape(s)

def title_block(parts, title, caption):
    parts.append(f'<text x="60" y="46" font-family="Arial,Helvetica,sans-serif" font-size="26" font-weight="bold" fill="{NAVY}">{esc(title)}</text>')
    parts.append(f'<text x="60" y="74" font-family="Arial,Helvetica,sans-serif" font-size="15" fill="{SUB}">{esc(caption)}</text>')
    parts.append(f'<line x1="60" y1="88" x2="1140" y2="88" stroke="{NAVY}" stroke-width="2"/>')

def group(parts, x, y, w, h, label):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="none" stroke="{NAVY}" stroke-width="1.5" stroke-dasharray="7 5"/>')
    parts.append(f'<text x="{x+14}" y="{y+22}" font-family="Arial,Helvetica,sans-serif" font-size="13" font-weight="bold" fill="{NAVY}" letter-spacing="1">{esc(label)}</text>')

def box(parts, x, y, w, h, title, subs=(), fill="#FFFFFF", title_size=16):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{BORDER}" stroke-width="1.5"/>')
    cy = y + 30 if subs else y + h / 2 + 6
    parts.append(f'<text x="{x+w/2}" y="{cy}" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="{title_size}" font-weight="bold" fill="{NAVY}">{esc(title)}</text>')
    for i, s in enumerate(subs):
        parts.append(f'<text x="{x+w/2}" y="{cy+24+i*20}" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="13" fill="{SUB}">{esc(s)}</text>')

def bar(parts, x, y, w, h, text, fill=NAVY, size=15):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}"/>')
    parts.append(f'<text x="{x+w/2}" y="{y+h/2+6}" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="{size}" font-weight="bold" fill="#FFFFFF">{esc(text)}</text>')

def arrow_down(parts, x, y1, y2):
    parts.append(f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{NAVY}" stroke-width="2" marker-end="url(#arr)"/>')

def arrow_right(parts, x1, x2, y):
    parts.append(f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{NAVY}" stroke-width="2" marker-end="url(#arr)"/>')

def footer(parts, y, text):
    parts.append(f'<text x="600" y="{y}" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="13" fill="{SUB}">{esc(text)}</text>')

def svg_open(h):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}">', DEFS,
            f'<rect x="0" y="0" width="{W}" height="{h}" fill="#FFFFFF"/>']

def save(name, parts, h):
    parts.append('</svg>')
    path = os.path.join(OUT, name)
    with open(path, 'w') as f:
        f.write("\n".join(parts))
    print(f"wrote {path} ({os.path.getsize(path)} bytes)")

# ---------------------------------------------------------------- 1. BASE
def base():
    h = 1000
    p = svg_open(h)
    title_block(p, "Base Platform Architecture",
                "One blueprint for every project: single-source or multi-source, per use case.")
    # Sources group
    group(p, 40, 108, 1120, 128, "SOURCES  ·  single-source or multi-source, per use case")
    srcs = [("APIs", ["REST · events"]), ("SQL DATABASES", ["queries · CDC"]),
            ("MySQL", ["app databases"]), ("FILES", ["CSV · JSON · Parquet"]),
            ("MFT", ["managed transfers"]), ("SFTP", ["partner drops"])]
    for i, (t, s) in enumerate(srcs):
        box(p, 60 + i * 188, 140, 172, 78, t, s, title_size=15)
    arrow_down(p, 600, 236, 258)
    bar(p, 40, 258, 1120, 46, "GATE:  SCHEMA CHECK  +  DATA QUALITY CHECK   ·   failures are quarantined, nothing bad lands")
    arrow_down(p, 600, 304, 326)
    # Pipeline group
    group(p, 40, 326, 1120, 158, "PIPELINE")
    box(p, 60, 360, 350, 104, "GLUE  →  SOURCE LAYER", ["loads as-arrived, full fidelity", "replayable · nothing lost"])
    box(p, 425, 360, 350, 104, "TRANSFORMATIONS  (PySpark)", ["joins · cleaning · dedupe", "business rules applied once, here"])
    box(p, 790, 360, 350, 104, "PREPARED TABLES", ["clean · conformed · modelled", "one version of the truth"])
    arrow_right(p, 410, 425, 412)
    arrow_right(p, 775, 790, 412)
    arrow_down(p, 965, 484, 506)
    bar(p, 40, 506, 1120, 46, "SEMANTIC LAYER  ·  Iceberg tables, filtered and promoted  ·  filter packages: row level · table level · field level")
    # Paths
    group(p, 40, 576, 550, 258, "PATH 1  ·  WITH DASHBOARD")
    box(p, 60, 612, 510, 76, "DASHBOARDS", ["QuickSight · Tableau · Power BI, on semantic tables"])
    arrow_down(p, 315, 688, 708)
    box(p, 60, 708, 510, 76, "BUSINESS USERS", ["finance · leadership · operations view and decide"])
    group(p, 610, 576, 550, 258, "PATH 2  ·  WITHOUT DASHBOARD")
    box(p, 630, 612, 164, 96, "SQL ACCESS", ["Athena / Trino", "analysts query directly"], title_size=14)
    box(p, 808, 612, 164, 96, "REST APIs", ["services consume", "programmatically"], title_size=14)
    box(p, 986, 612, 154, 96, "FILTER PACKAGES", ["row · table · field", "feeds · shares · ML"], title_size=14)
    box(p, 630, 724, 510, 60, "DOWNSTREAM SYSTEMS  ·  ANALYSTS  ·  ML MODELS", [], title_size=14)
    bar(p, 40, 858, 1120, 46, "PLATFORM:  Airflow orchestration  ·  daily DQ checks (delta detection)  ·  CloudWatch monitoring + alerts  ·  Terraform + CI/CD", fill=GREY)
    footer(p, 940, "Generic clean-room recreation  ·  synthetic data only  ·  no company or proprietary details")
    save("base-platform-architecture.svg", p, h)

# ---------------------------------------------------------------- 2. CRM
def crm():
    h = 940
    p = svg_open(h)
    title_block(p, "Redesigned Ingestion — CRM",
                "After: the data decides. The watermark is read from the target itself.")
    bar(p, 60, 108, 1080, 46, "AFTER  ·  RUN LOGIC: THE DATA DECIDES  ·  watermark read from the target itself")
    arrow_down(p, 600, 154, 176)
    box(p, 60, 176, 520, 92, "CRM API  (e.g. Salesforce)", ["queries are built per table, from the watermark"], title_size=16)
    box(p, 620, 176, 520, 92, "CUSTOM DOWNLOADERS  (Glue)", ["for each table: Athena MAX(timestamp) first,", "then the API query since that watermark"], title_size=16)
    arrow_right(p, 580, 620, 222)
    arrow_down(p, 880, 268, 290)
    box(p, 60, 290, 1080, 74, "RAW LAYER", ["JSON, exactly as the API returned it"], title_size=16)
    bar(p, 60, 384, 1080, 46, "SCHEMA CHECK  ·  RAW → SRC  ·  SRC tables are written only after the check passes")
    box(p, 60, 450, 350, 96, "SRC JOB  →  SRC LAYER", ["overwrite that day's load"], title_size=15)
    box(p, 425, 450, 350, 96, "PRE JOB  →  PRE LAYER", ["upsert · PRE holds the history"], title_size=15)
    box(p, 790, 450, 350, 96, "SEM JOB  →  SEM LAYER", ["Iceberg → Iceberg promotion · fast"], title_size=15)
    arrow_right(p, 410, 425, 498)
    arrow_right(p, 775, 790, 498)
    arrow_down(p, 965, 546, 568)
    box(p, 60, 568, 1080, 74, "CONSUMERS", ["dashboards · downstream teams read SEM"], title_size=16)
    bar(p, 60, 662, 1080, 46, "DQ ON SEM  ·  EVERY DAY AT NOON  ·  timestamp field checked  ·  no new data → alert", fill=GREY)
    bar(p, 60, 728, 1080, 64, "SELF-HEALING:  DOWN 1 DAY OR 10, THE NEXT RUN RESUMES FROM THE WATERMARK  ·  NO GAPS · NO FULL RELOADS · CATCH-UP IS AUTOMATIC", size=14)
    footer(p, 830, "Generic clean-room recreation  ·  synthetic data only  ·  no company or proprietary details")
    save("crm-ingestion.svg", p, h)

# ---------------------------------------------------------------- 3. KAFKA
def kafka():
    h = 1000
    p = svg_open(h)
    title_block(p, "Streaming Ingestion — Kafka / Kinesis",
                "Same base layers as the platform blueprint, with streaming sources and replay.")
    group(p, 40, 108, 1120, 128, "EVENT SOURCES  ·  continuous, ordered, replayable")
    srcs = [("KAFKA TOPICS", ["ordered events"]), ("KINESIS STREAMS", ["real-time ingest"]),
            ("EVENT PRODUCERS", ["apps · services"]), ("API EVENTS", ["webhooks · REST"]),
            ("CDC", ["database changes"]), ("FILES", ["CSV · JSON · Parquet"])]
    for i, (t, s) in enumerate(srcs):
        box(p, 60 + i * 188, 140, 172, 78, t, s, title_size=15)
    arrow_down(p, 600, 236, 258)
    bar(p, 40, 258, 1120, 46, "GATE:  SCHEMA CHECK  +  DATA QUALITY CHECK   ·   bad events are quarantined, nothing bad lands")
    arrow_down(p, 600, 304, 326)
    group(p, 40, 326, 1120, 158, "STREAMING PIPELINE")
    box(p, 60, 360, 350, 104, "STREAM INGESTION", ["Kafka / Kinesis consumers", "offsets tracked · replayable"])
    box(p, 425, 360, 350, 104, "STREAM PROCESSING  (PySpark)", ["joins · cleaning · dedupe", "late data handled · windows"])
    box(p, 790, 360, 350, 104, "PREPARED TABLES", ["clean · conformed · modelled", "one version of the truth"])
    arrow_right(p, 410, 425, 412)
    arrow_right(p, 775, 790, 412)
    arrow_down(p, 965, 484, 506)
    bar(p, 40, 506, 1120, 46, "SEMANTIC LAYER  ·  Iceberg tables, filtered and promoted  ·  filter packages: row level · table level · field level")
    group(p, 40, 576, 550, 258, "PATH 1  ·  WITH DASHBOARD")
    box(p, 60, 612, 510, 76, "DASHBOARDS", ["QuickSight · Tableau · Power BI, on semantic tables"])
    arrow_down(p, 315, 688, 708)
    box(p, 60, 708, 510, 76, "BUSINESS USERS", ["finance · leadership · operations view and decide"])
    group(p, 610, 576, 550, 258, "PATH 2  ·  WITHOUT DASHBOARD")
    box(p, 630, 612, 164, 96, "SQL ACCESS", ["Athena / Trino", "analysts query directly"], title_size=14)
    box(p, 808, 612, 164, 96, "REST APIs", ["services consume", "programmatically"], title_size=14)
    box(p, 986, 612, 154, 96, "FILTER PACKAGES", ["row · table · field", "feeds · shares · ML"], title_size=14)
    box(p, 630, 724, 510, 60, "DOWNSTREAM SYSTEMS  ·  ANALYSTS  ·  ML MODELS", [], title_size=14)
    bar(p, 40, 858, 1120, 46, "EXACTLY-ONCE  ·  idempotent writes  ·  replay from any offset  ·  late data reprocessed, not lost", fill=GREY)
    footer(p, 940, "Generic clean-room recreation  ·  synthetic data only  ·  no company or proprietary details")
    save("kafka-streaming-ingestion.svg", p, h)

# ---------------------------------------------------------------- 4. ICEBERG
def iceberg():
    h = 940
    p = svg_open(h)
    title_block(p, "Hive to Iceberg — Lakehouse Migration",
                "Same data, new table format: backfill, validate side by side, then cut over.")
    group(p, 40, 108, 1120, 128, "SOURCE  ·  as it was")
    box(p, 60, 140, 520, 78, "HIVE TABLES", ["existing warehouse tables"])
    box(p, 620, 140, 520, 78, "HIVE METASTORE", ["schema · partitions · history"])
    arrow_down(p, 320, 218, 240)
    arrow_down(p, 880, 218, 240)
    bar(p, 40, 240, 1120, 46, "MIGRATION  ·  backfill in stages, table by table  ·  no big-bang cutover")
    arrow_down(p, 600, 286, 308)
    group(p, 40, 308, 1120, 158, "MIGRATION PIPELINE")
    box(p, 60, 342, 350, 104, "BACKFILL  (Spark)", ["Hive → Iceberg, in stages", "replayable · nothing lost"])
    box(p, 425, 342, 350, 104, "DUAL-RUN VALIDATION", ["row counts · checksums", "Hive vs Iceberg, side by side"])
    box(p, 790, 342, 350, 104, "CUTOVER", ["one table at a time", "roll back with a snapshot"])
    arrow_right(p, 410, 425, 394)
    arrow_right(p, 775, 790, 394)
    arrow_down(p, 965, 466, 488)
    bar(p, 40, 488, 1120, 46, "ICEBERG TARGET  ·  snapshot time travel  ·  roll back a bad load  ·  ACID upserts")
    group(p, 40, 558, 1120, 200, "CONSUMERS  ·  on Iceberg")
    box(p, 60, 592, 350, 96, "DASHBOARDS", ["QuickSight · Tableau · Power BI"])
    box(p, 425, 592, 350, 96, "SQL ACCESS", ["Athena / Trino", "analysts query directly"])
    box(p, 790, 592, 350, 96, "ML FEATURES", ["features read from gold", "training · scoring"])
    bar(p, 40, 778, 1120, 46, "PLATFORM:  Airflow orchestration  ·  daily DQ checks  ·  CloudWatch monitoring + alerts  ·  Terraform + CI/CD", fill=GREY)
    footer(p, 864, "Generic clean-room recreation  ·  synthetic data only  ·  no company or proprietary details")
    save("iceberg-lakehouse.svg", p, h)

# ---------------------------------------------------------------- 5. ML
def ml():
    h = 940
    p = svg_open(h)
    title_block(p, "Demand Forecasting — ML on the Gold Layer",
                "From curated gold tables to a forecast a team can act on, with backtesting.")
    group(p, 40, 108, 1120, 128, "INPUT  ·  curated gold layer")
    box(p, 60, 140, 350, 78, "GOLD TABLES", ["dimensional · SCD 1/2"])
    box(p, 425, 140, 350, 78, "DEMAND HISTORY", ["per product · per region"])
    box(p, 790, 140, 350, 78, "REFERENCE DATA", ["calendar · seasonality"])
    arrow_down(p, 235, 218, 240)
    arrow_down(p, 600, 218, 240)
    arrow_down(p, 965, 218, 240)
    bar(p, 40, 240, 1120, 46, "FEATURE ENGINEERING  ·  lag demand  ·  rolling means  ·  seasonality by month  ·  region mix")
    arrow_down(p, 600, 286, 308)
    group(p, 40, 308, 1120, 158, "MODEL")
    box(p, 60, 342, 350, 104, "TRAINING", ["baseline + seasonal model", "features use only past data"])
    box(p, 425, 342, 350, 104, "BACKTESTING", ["last 90 days held out", "MAE reported · no leakage"])
    box(p, 790, 342, 350, 104, "SCORING", ["next 30 days, per product", "plain-English driver summary"])
    arrow_right(p, 410, 425, 394)
    arrow_right(p, 775, 790, 394)
    arrow_down(p, 965, 466, 488)
    bar(p, 40, 488, 1120, 46, "CONSUMERS  ·  dashboards  ·  planning teams  ·  downstream systems read the forecast")
    group(p, 40, 558, 1120, 200, "CONSUMERS")
    box(p, 60, 592, 350, 96, "DASHBOARDS", ["forecast vs actual", "drivers behind the number"])
    box(p, 425, 592, 350, 96, "PLANNING TEAMS", ["view and decide", "per product · per region"])
    box(p, 790, 592, 350, 96, "DOWNSTREAM SYSTEMS", ["forecasts consumed", "programmatically"])
    bar(p, 40, 778, 1120, 46, "MONITORING:  daily DQ checks  ·  forecast drift watched  ·  model retrained on fresh gold data", fill=GREY)
    footer(p, 864, "Generic clean-room recreation  ·  synthetic data only  ·  no company or proprietary details")
    save("ml-demand-forecasting.svg", p, h)

if __name__ == "__main__":
    base(); crm(); kafka(); iceberg(); ml()
    print("done")
