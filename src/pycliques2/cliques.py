from functools import singledispatch
import networkx as nx
import itertools
import math


class Clique(frozenset):
    """Base class for a clique in a graph.

    This class derives from :class:`frozenset` but overrides ``__repr__`` so
    that instances display like plain set literals instead of ``frozenset``.

    .. rubric:: Examples

    Inspecting a non-empty clique produces a clean set-style representation::

        >>> from pycliques2 import Clique
        >>> Clique({1, 2, 3})
        {1, 2, 3}

    Empty cliques render as ``{}``, which keeps doctest outputs short and lets
    documentation examples double as regression tests::

        >>> Clique([])
        {}
    """
    def __repr__(self):
        """Return a set-style string representation for doctest friendliness."""
        u = set(self)
        if len(u) == 0:
            return "{}"
        else:
            return f"{u}"


@singledispatch
def clique_graph(graph, bound=math.inf):
    """Produce the clique graph of an undirected NetworkX graph.

    .. rubric:: Parameters

    graph : networkx.Graph
        Input graph whose cliques will become nodes of the output graph.
    bound : int, optional
        Maximum number of cliques to allow before aborting (default: ``math.inf``).

    .. rubric:: Returns

    networkx.Graph | None
        The clique graph if the clique count stays within ``bound``; ``None``
        otherwise.

    .. rubric:: Examples

    >>> import networkx as nx
    >>> from pycliques2 import Clique, clique_graph
    >>> g = clique_graph(nx.octahedral_graph())
    >>> g.number_of_nodes()
    8
    >>> g.degree[Clique({0, 1, 2})]
    6
    >>> clique_graph(nx.cycle_graph(4), bound=2) is None
    True
    """
    it_cliques = nx.find_cliques(graph)
    cliques = []
    K = nx.Graph()
    while True:
        try:
            clique = next(it_cliques)
            cliques.append(Clique(clique))
            if len(cliques) > bound:
                return None
        except StopIteration:
            break
    K.add_nodes_from(cliques)
    clique_pairs = itertools.combinations(cliques, 2)
    K.add_edges_from((c1, c2) for (c1, c2) in clique_pairs if c1 & c2)
    return K
