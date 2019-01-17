from scipy import stats as _stats


class _frozen(_stats._distn_infrastructure.rv_frozen):
    def __init__(self, dist, *args, **kwds):
        super(_frozen, self).__init__(dist, *args, **kwds)


def buniform(a=0, b=1):
    """
    A uniform continuous random variable.

    Without arguments, the distribution is uniform on [0, 1]. 
    Use the parameters `a` and `b` to obtain a uniform distribution on [a, b].
    The returned object has the same generic methods as other scipy.stats distributions.
    """
    dist = _stats.uniform
    dist.name = 'uniform'
    return _frozen(dist, loc=a, scale=b - a)
