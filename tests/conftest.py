"""Shared pytest fixtures for the medallion platform tests."""

import pytest

from src.spark.session import build_session


@pytest.fixture(scope="session")
def spark():
    """Session-scoped SparkSession shared across all tests.

    Creating a SparkSession is expensive (~5-10 seconds), so we build once per
    test session and tear down at the end.
    """
    session = build_session(app_name="medallion-tests")
    yield session
    session.stop()
