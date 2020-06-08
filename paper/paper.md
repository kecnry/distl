---
title: 'distl: simplified and condensed distributions in Python'
tags:
  - Python
  - distributions
  - statistics
authors:
  - name: Kyle E. Conroy
    orcid: 0000-0002-5442-8550
    affiliation: "1" # (Multiple affiliations must be quoted)
affiliations:
 - name: Department of Astrophysics & Planetary Sciences, Villanova University, USA
   index: 1
date: 20 May 2020
bibliography: paper.bib
---

# Summary

Many applications call for either sampling from a probability density function or determining the probability of drawing a specific value.  For example, using an Markov-Chain Monte Carlo code such as `emcee` `[@emcee; @emceev3]`, the user has to both provide the initial position of the walkers (often by drawing from a distribution) as well as a callable function which returns the log-likelihood, which in turn needs to include the log-probability of drawing each of the sampled values from the desired priors.  This generally requires manually creating or adjusting the callable function for any specific set of priors and sampled values, but is not convenient to do programatically.

`distl` is a Python package which allows for defining, combining, plotting, serializing, and exposing statistics or sampling from complex probability distributions.  Whenever possible, the underlying distributions are handled by the appropriate functions in `scipy.stats` `[@scipy]`, with unit conversion and support handled by `astropy` `[@astropy]`, and plotting support through `matplotlib` `[@matplotlib]` and `corner` `[@corner]`.  Currently, `distl` includes support for the following distribution types: delta, uniform (boxcar), gaussian (normal), histogram, samples (KDE representation of an existing set of samples from the distribution), multivariate gaussian, multivariate histogram, and multivariate samples.  With few exceptions, all of these distribution types can be combined with any of the following math operations: addition, subtraction, multiplication, division, power, and, or, as well as trig operators.  Whenever possible, the resulting composite distribution maintains any covariances from underlying multivariate distributions.

As all these distribution objects can be serialized and deserialized and have a common interface for sampling and calculating probabilities, it becomes easy to generate these complex distributions and pass them through other codes flexibly.  For example, in the `emcee` case mentioned earlier, the log-probability function can remain fixed, only needing to loop over the provided set of priors and call the `logp` methods to account for the log-priors term in the log-likelihood.

`distl` was designed to be used in `PHOEBE` `[@prsa2016; @horvat2018; @jones2020]` - a software package to model eclipse binaries - as part of a release to support solving the inverse problem with optimizers and samplers (including `emcee`).  With `distl`, `PHOEBE` now allows the user to easily define and manipulate distributions, as priors, sampling distributions, or to process results from samplers into posteriors.

`distl` is hosted at the [GitHub repository](https://github.com/kecnry/distl), with documentation at [distl.readthedocs.io](https://distl.readthedocs.io), and is available for installation via `pip install distl`.

# Examples

Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Fenced code blocks are rendered with syntax highlighting:
```python
for n in range(10):
    yield f(n)
```

# Acknowledgements

Thanks to many discussions and feedback from Andrej Prsa and Angela Kochoska.

# References
