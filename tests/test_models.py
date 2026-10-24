"""
Tests for model-related functionality.
"""

from sklearn.linear_model import LogisticRegression


def test_model_instantiation():
    """
    Verify that a model object can be created.
    """

    model = LogisticRegression()

    assert model is not None


def test_model_has_fit_method():
    """
    Verify that training functionality exists.
    """

    model = LogisticRegression()

    assert hasattr(model, "fit")