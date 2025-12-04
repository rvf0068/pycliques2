from pycliques2.cliques import Clique


def test_clique_creation():
    """Test that we can create a clique from a list or set."""
    c = Clique([1, 2, 3])
    assert 1 in c
    assert len(c) == 3
    assert isinstance(c, frozenset)


def test_clique_repr():
    """Test the custom string representation."""
    c = Clique([1, 2])
    # The set order isn't guaranteed, so we check both possibilities
    assert repr(c) == "{1, 2}" or repr(c) == "{2, 1}"


def test_empty_clique_repr():
    """Test the representation of an empty clique."""
    c = Clique([])
    assert repr(c) == "{}"


def test_clique_equality():
    """Test that Cliques compare equal to standard sets/frozensets."""
    c = Clique([1, 2])
    assert c == {1, 2}
    assert c == frozenset([1, 2])
