"""Base pipeline abstraction using Template Method pattern.

Day 1: Design this class with:
- __init__(config: dict) to accept pipeline configuration
- Abstract methods: extract(), transform(), load()
- Concrete run() method that calls extract -> transform -> load in order

This is the foundation all other pipelines inherit from.
"""
from abc import ABC, abstractmethod


class BasePipeline(ABC):
    """Abstract base for all data pipelines.

    Implements the Template Method pattern: run() defines the skeleton,
    subclasses fill in extract/transform/load.
    """

    def __init__(self, config: dict):
        # TODO (Day 1): Store config, initialize SparkSession or other shared state
        pass

    @abstractmethod
    def extract(self):
        """Read data from source. Returns a DataFrame."""
        ...

    @abstractmethod
    def transform(self, df):
        """Apply transformations. Returns a transformed DataFrame."""
        ...

    @abstractmethod
    def load(self, df):
        """Write data to destination."""
        ...

    def run(self):
        """Execute the full pipeline: extract -> transform -> load."""
        # TODO (Day 1): Implement the template method
        pass
