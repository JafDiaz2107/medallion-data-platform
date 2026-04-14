"""Sessionization strategy using time-gap logic.

Day 10: Group events into sessions based on inactivity gaps.
Uses window functions (LAG, ROW_NUMBER) to detect session boundaries.
"""
from .strategy import TransformStrategy


class SessionizationStrategy(TransformStrategy):
    """Groups user events into sessions based on time gaps.

    A new session starts when the gap between consecutive events
    exceeds session_timeout_minutes.
    """

    def __init__(self, session_timeout_minutes: int = 30):
        self.session_timeout_minutes = session_timeout_minutes

    def apply(self, df):
        """Sessionize events. Adds session_id and session_start columns."""
        # TODO (Day 10): Implement using window functions
        # 1. Partition by user_id, order by timestamp
        # 2. Use LAG to get previous event timestamp
        # 3. Flag new session when gap > timeout
        # 4. Use cumulative SUM to assign session_id
        pass
