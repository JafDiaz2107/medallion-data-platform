"""SparkSession factory with Delta Lake support.

Single entry point for creating a SparkSession across Bronze, Silver, and Gold
pipelines. Centralizing this prevents config drift between layers.
"""

import os

from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip


DEFAULT_JAVA_HOME = "/opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk/Contents/Home"


def build_session(
    app_name: str,
    master: str = "local[*]",
    warehouse_dir: str = "/tmp/medallion-warehouse",
    java_home: str | None = None,
) -> SparkSession:
    """Create a SparkSession configured for Delta Lake.

    Args:
        app_name: Identifier in Spark UI and cluster logs.
        master: Where Spark runs. "local[*]" for dev, "yarn" / "k8s://..." in prod.
        warehouse_dir: Default directory for managed SQL tables.
        java_home: Path to JDK. Defaults to Homebrew OpenJDK 17 on Apple Silicon.

    Returns:
        A SparkSession ready to read and write Delta tables via SQL and DataFrame APIs.
    """
    os.environ["JAVA_HOME"] = java_home or DEFAULT_JAVA_HOME

    builder = (
        SparkSession.builder.appName(app_name)
        .master(master)
        .config("spark.sql.warehouse.dir", warehouse_dir)
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )
        .config(
            "spark.sql.extensions",
            "io.delta.sql.DeltaSparkSessionExtension",
        )
    )

    spark = configure_spark_with_delta_pip(builder).getOrCreate()
    spark.sparkContext.setLogLevel("WARN")
    return spark
