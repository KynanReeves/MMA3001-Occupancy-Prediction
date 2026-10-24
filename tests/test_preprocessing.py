"""
Tests for preprocessing functionality.
"""

import pandas as pd


def test_dataframe_creation():
    """
    Verify that test data can be created in the expected format.
    """

    data = {
        "temperature": [22.5, 23.1],
        "humidity": [45, 50],
    }

    df = pd.DataFrame(data)

    assert len(df) == 2
    assert "temperature" in df.columns
    assert "humidity" in df.columns


def test_missing_value_detection():
    """
    Verify that missing values can be identified.
    """

    df = pd.DataFrame({
        "temperature": [22.5, None, 23.1]
    })

    assert df["temperature"].isna().sum() == 1