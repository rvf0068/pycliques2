class Clique(frozenset):
    """
    Base class for a clique in a graph.

    This class is derived from frozenset, but we modify its representation so
    that it does not print the word 'frozenset'.
    """
    def __repr__(self):
        u = set(self)
        if len(u) == 0:
            return "{}"
        else:
            return f"{u}"
