# Minimum Description Length Binning

This is an implementation of Usama Fayyad's entropy based
expert binning method.

*Fayyad, Usama M.; Irani, Keki B. (1993) "Multi-Interval Discretization of Continuous-Valued Attributes for Classification Learning" , Proceedings of the International Joint Conference on Uncertainty in AI (Q334 .I571 1993), pp. 1022-1027
[https://trs.jpl.nasa.gov/handle/2014/35171](https://trs.jpl.nasa.gov/handle/2014/35171)

Please read the original paper
<a href="http://sci2s.ugr.es/keel/pdf/algorithm/congreso/fayyad1993.pdf">here</a>
for more information.

# Tests

To run the unit tests, make sure you have `nose` installed. Afterwards,

```
$ make test
```

should do the trick.

# Installation and Usage

This code was built using Cython, so you have to run the makefile
in the directory.

```
$ pip3 install mdlp
```

```
>>> from mdlp import MDLP
>>> from sklearn.datasets import load_iris
>>> iris = load_iris()
>>> X = iris.data
>>> y = iris.target
>>> mdlp = MDLP()
>>> conv_X = mdlp.fit_transform(X, y)
```

I recommend creating a virtual environment for this project.
