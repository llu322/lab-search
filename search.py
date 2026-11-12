"""Search text documents and report matching lines and counts."""


def number_lines(lines):
    """Return (line_number, text) tuples, counting from 1.

    >>> number_lines(['Library hours', '', 'Open late'])
    [(1, 'Library hours'), (2, ''), (3, 'Open late')]
    >>> number_lines([])
    []
    """
    return list(enumerate(lines, start=1))


def matching_lines(lines, query):
    """Return numbered lines containing query, ignoring case.

    An empty query returns no matches. Preserve the original text and numbers.

    >>> matching_lines(['Library hours', '', 'LIBRARY cafe'], 'library')
    [(1, 'Library hours'), (3, 'LIBRARY cafe')]
    >>> matching_lines(['Library hours'], '')
    []
    >>> matching_lines(['Library hours'], 'pool')
    []
    """
    if query == '':
        return []

    return [
        (number, text)
        for number, text in number_lines(lines)
        if query.lower() in text.lower()
    ]


def group_matches(documents, query):
    """Return one list of matching lines per document, including empty lists.

    >>> group_matches([['Library map'], ['Pool hours'], ['LIBRARY cafe']], 'library')
    [[(1, 'Library map')], [], [(1, 'LIBRARY cafe')]]
    >>> group_matches([], 'library')
    []
    """
    return [matching_lines(document, query) for document in documents]


def flatten_matches(names, groups):
    """Return (filename, line_number, text) tuples in file and line order.

    names and groups have equal lengths. Filenames are unique.

    >>> flatten_matches(['a.txt', 'b.txt'], [[(2, 'Map')], []])
    [('a.txt', 2, 'Map')]
    >>> flatten_matches([], [])
    []
    """
    return [
        (name, number, text)
        for name, group in zip(names, groups)
        for number, text in group
    ]


def match_counts(names, groups):
    """Return a dictionary of filename: number of matching lines, including zeros.

    names and groups have equal lengths. Filenames are unique.

    >>> match_counts(['a.txt', 'b.txt'], [[(2, 'Map')], []])
    {'a.txt': 1, 'b.txt': 0}
    >>> match_counts([], [])
    {}
    """
    return {name: len(group) for name, group in zip(names, groups)}