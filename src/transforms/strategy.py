"""Transform strategy interface.

Day 9: Define the contract for swappable transformation logic.
Each strategy takes a DataFrame and returns a transformed DataFrame.
"""
from abc import ABC, abstractmethod


class TransformStrategy(ABC):
    """Interface for pipeline transformation strategies."""

    @abstractmethod
    def apply(self, df):
        """Apply transformation to DataFrame. Returns transformed DataFrame."""
        ...
