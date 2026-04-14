"""Data validation framework using Strategy pattern.

Day 3: Implement a validator that holds a list of validation rules.
Each rule splits a DataFrame into passed and failed records.
Failed records go to a quarantine path for investigation.
"""


class ValidationRule:
    """A single validation rule that can be applied to a DataFrame."""

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def validate(self, df):
        """Apply validation. Returns (passed_df, failed_df)."""
        # TODO (Day 3): Implement in concrete subclasses
        raise NotImplementedError


class DataValidator:
    """Applies a list of validation rules to a DataFrame.

    Usage:
        validator = DataValidator([NullCheckRule("email"), ...])
        clean_df, quarantine_df = validator.run(df)
    """

    def __init__(self, rules: list[ValidationRule] = None):
        self.rules = rules or []

    def add_rule(self, rule: ValidationRule):
        # TODO (Day 3): Add a rule to the validator
        pass

    def run(self, df):
        """Apply all rules sequentially. Returns (passed_df, quarantine_df)."""
        # TODO (Day 3): Implement — chain rules, accumulate quarantined records
        pass
