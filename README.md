### A better scipy.stats.uniform

The `stats` sub-package of scipy is quite cool.  
In particular, it provides dozens of probability distributions implemented with
a common interface.

But `scipy.stats.uniform` always bugged me.


```python
>>> from scipy import stats
>>> help(stats.uniform)

A uniform continuous random variable.
  
This distribution is constant between `loc` and ``loc + scale``.
```

Why `loc + scale`? Why not `scale`?  

So I wrote `better_uniform`: eight small lines of code that don't bug me so
much.


```python
from scipy import stats 

class frozen(stats._distn_infrastructure.rv_continuous_frozen):
    def __init__(self, dist, *args, **kwds):
        super(frozen,self).__init__(dist, *args, **kwds)

def buniform(a, b):  # b for better
    dist = stats.uniform
    dist.name = 'uniform'
    return frozen(dist, loc=a, scale=b-a)
```


Now it works as I expect it to work:

```python
d = buniform(0, 1)
d.rvs()      # 0 < rv < 1
d.suport()   # (0.0, 1.0)

d = buniform(1, 2)
d.rvs()      # 1 < rv < 2
d.support()  # (1.0, 2.0)

# note the difference
from scipy.stats import uniform
d = uniform(1, 2)
d.rvs()      # 1 < rv < 3
d.support()  # (1.0, 3.0)
```



That's it!


#### Cool, I want it!

```
pip install better-uniform
```

or 

```bash
git clone https://github.com/j-faria/better_uniform.git
cd better_uniform
python setup.py install
```

and later, from Python

```python
from better_uniform import buniform
```

or better yet

```python
from better_uniform import buniform as uniform
```


