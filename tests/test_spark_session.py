"""Smoke tests for the SparkSession factory."""


def test_session_is_delta_enabled(spark):
    """The SparkSession must have Delta Lake's catalog and SQL extensions wired up."""
    catalog = spark.conf.get("spark.sql.catalog.spark_catalog")
    extensions = spark.conf.get("spark.sql.extensions")

    assert catalog == "org.apache.spark.sql.delta.catalog.DeltaCatalog"
    assert "DeltaSparkSessionExtension" in extensions


def test_session_can_create_dataframe(spark):
    """Basic sanity check: the SparkSession can create and count a DataFrame."""
    df = spark.range(10)
    assert df.count() == 10
