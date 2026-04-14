"""Tests for pipeline classes.

Day 5: Write unit tests for BasePipeline, BatchPipeline, StreamPipeline.
Mock Spark dependencies. Test the template method pattern works correctly.
"""
import pytest


class TestBatchPipeline:
    """Tests for BatchPipeline."""

    # TODO (Day 5): Test extract reads data correctly
    # TODO (Day 5): Test transform applies cleaning rules
    # TODO (Day 5): Test load writes to Delta
    # TODO (Day 5): Test run() calls extract -> transform -> load in order
    pass


class TestStreamPipeline:
    """Tests for StreamPipeline."""

    # TODO (Day 5): Test watermark configuration
    # TODO (Day 5): Test trigger interval settings
    pass
