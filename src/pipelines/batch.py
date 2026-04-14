"""Batch pipeline for Bronze layer ingestion.

Day 2: Implement concrete methods for reading source files
and writing to Delta format with appropriate modes and partitioning.
"""
from .base import BasePipeline


class BatchPipeline(BasePipeline):
    """Batch ingestion pipeline: source files -> Delta tables."""

    def extract(self):
        # TODO (Day 2): Read source data (CSV/JSON/Parquet)
        pass

    def transform(self, df):
        # TODO (Day 3): Apply Silver layer transformations
        pass

    def load(self, df):
        # TODO (Day 2): Write to Delta with partitioning and write mode
        pass

    def read_source(self, path: str, format: str = "csv"):
        """Read from a source path in the given format."""
        # TODO (Day 2): Implement with schema inference or explicit StructType
        pass

    def write_delta(self, df, path: str, mode: str = "append"):
        """Write DataFrame to Delta format."""
        # TODO (Day 2): Implement with partition strategy
        pass
