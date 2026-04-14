"""Cost monitoring with Observer pattern for alerting.

Day 15: Track compute costs per pipeline run.
Day 16: Add recommend_optimization() based on cost history.
Day 18: Integrate into pipeline classes via dependency injection.
"""


class CostMonitor:
    """Tracks and analyzes pipeline compute costs.

    Usage:
        monitor = CostMonitor(threshold_dbu=100)
        monitor.log_run(pipeline_name, dbu_consumed, duration_sec)
        monitor.recommend_optimization()
    """

    def __init__(self, threshold_dbu: float = 100.0):
        self.threshold_dbu = threshold_dbu
        self.history = []

    def log_run(self, pipeline_name: str, dbu_consumed: float, duration_sec: float):
        """Log a pipeline run's cost data."""
        # TODO (Day 15): Store run data, check against threshold, alert if exceeded
        pass

    def get_cost_summary(self):
        """Return cost summary across all logged runs."""
        # TODO (Day 15): Aggregate cost history
        pass

    def recommend_optimization(self):
        """Analyze cost history and suggest optimizations."""
        # TODO (Day 16): Analyze patterns, suggest changes
        # e.g., "Switch Bronze to spot instances", "Reduce Gold cluster size"
        pass
