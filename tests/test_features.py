"""
Tests for feature engineering functionality.
"""

import pandas as pd


def test_hour_feature_extraction():
    """
    Verify that timestamps can be converted into hour values.
    """

    timestamps = pd.to_datetime([
        "2026-01-01 09:00:00",
        "2026-01-01 15:00:00"
    ])

    hours = timestamps.hour

    assert hours[0] == 9
    assert hours[1] == 15


def test_weekend_detection():
    """
    Verify weekday/weekend identification logic.
    """

    dates = pd.to_datetime([
        "2026-01-02",  # Friday
        "2026-01-03"   # Saturday
    ])

    is_weekend = dates.dayofweek >= 5

    assert is_weekend[0] is False
    assert is_weekend[1] is True