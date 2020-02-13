def gini2(c1, c2):
    """
    Calculates the gini impurity for binary class data.

    Parameters
    ----------
    c1 : int
        Number of examples of class 1
    c2 : int
        Number of examples of class 2

    Returns
    -------
    float
        The gini impurity
    """
    n = c1 + c2  # total examples
    p1 = c1 / n  # proportion of instance that are class 1
    p2 = c2 / n  # proportion of instance that are class 2
    return p1*(1-p1) + p2*(1-p2)  # calculate gini impurity