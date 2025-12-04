class Clique(frozenset):
    """Base class for a clique in a graph.

    This class derives from :class:`frozenset` but overrides ``__repr__`` so
    that instances display like plain set literals instead of ``frozenset``.

    Examples
    --------

    Inspecting a non-empty clique produces a clean set-style representation::

        >>> from pycliques2.cliques import Clique
        >>> Clique({1, 2, 3})
        {1, 2, 3}

    Empty cliques render as ``{}``, which keeps doctest outputs short and lets
    documentation examples double as regression tests::

        >>> Clique([])
        {}
    """
    def __repr__(self):
        u = set(self)
        if len(u) == 0:
            return "{}"
        else:
            return f"{u}"
