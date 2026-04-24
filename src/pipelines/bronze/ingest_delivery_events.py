"""Bronze layer: raw delivery event ingestion to Delta Lake.

Reads source events (JSON) and writes them as a Delta table with no transformation.
Bronze is the source of truth — cleaning happens in Silver.
"""

from pyspark.sql import DataFrame, SparkSession


def ingest(
    spark: SparkSession,
    source_path: str,
    bronze_path: str,
    mode: str = "overwrite",
) -> DataFrame:
    """Read raw delivery events and land them in the Bronze Delta table.

    Args:
        spark: Active SparkSession configured for Delta Lake.
        source_path: Path to source data (JSON, CSV, or Parquet).
        bronze_path: Destination path for the Bronze Delta table.
        mode: Write mode. "overwrite" for full refresh, "append" for incremental.

    Returns:
        The DataFrame that was written, ready for downstream inspection.
    """
    df = spark.read.json(source_path)
    df.write.format("delta").mode(mode).save(bronze_path)
    return df
