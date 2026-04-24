"""Demo CLI: ingest sample delivery events into the Bronze Delta table.

Run from the repo root:
    python scripts/run_bronze_ingest.py
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from src.pipelines.bronze.ingest_delivery_events import ingest  # noqa: E402
from src.spark.session import build_session  # noqa: E402

SOURCE_PATH = REPO_ROOT / "data" / "sample" / "delivery_events.json"
BRONZE_PATH = "/tmp/medallion-bronze/delivery_events"


def main() -> None:
    spark = build_session(app_name="bronze-ingest-delivery-events")

    df = ingest(
        spark=spark,
        source_path=str(SOURCE_PATH),
        bronze_path=BRONZE_PATH,
        mode="overwrite",
    )

    print(f"Ingested {df.count()} events into Bronze at {BRONZE_PATH}")
    print("Schema:")
    df.printSchema()
    df.show(truncate=False)

    spark.stop()


if __name__ == "__main__":
    main()
