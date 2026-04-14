"""Streaming pipeline with watermark and checkpoint support.

Day 4 (signature) + Day 9 (full implementation):
Configure structured streaming with watermark for late data,
trigger intervals, and output modes.
"""
from .base import BasePipeline


class StreamPipeline(BasePipeline):
    """Streaming pipeline: real-time events -> Delta/Iceberg tables."""

    def __init__(self, config: dict):
        super().__init__(config)
        # TODO (Day 4): Add watermark_duration, trigger_interval, output_mode

    def extract(self):
        # TODO (Day 9): Structured streaming read from source
        pass

    def transform(self, df):
        # TODO (Day 9): Apply watermark and streaming transformations
        pass

    def load(self, df):
        # TODO (Day 9): Streaming write with trigger and checkpoint
        pass
