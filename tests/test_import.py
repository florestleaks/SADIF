"""Test sadif."""

import sadif


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(sadif.__name__, str)
