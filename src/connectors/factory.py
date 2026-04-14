"""Data source factory for multiple table formats.

Day 8: Factory pattern that creates the right connector
based on the requested format (Delta, Iceberg, CSV).
"""


class DataSourceFactory:
    """Creates data source connectors for different table formats.

    Usage:
        factory = DataSourceFactory(spark)
        reader = factory.create("delta")
        df = reader.read(path)
    """

    def __init__(self, spark):
        self.spark = spark

    def create(self, format: str):
        """Create a data source connector for the given format.

        Args:
            format: One of "delta", "iceberg", "csv", "parquet"

        Returns:
            A connector with a common read/write interface.
        """
        # TODO (Day 8): Implement factory logic
        # Return DeltaSource, IcebergSource, or CSVSource
        pass
