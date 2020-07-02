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

Many scientific and statistical applications require either sampling from a probability density function (PDF) or determining the probability of drawing a specific value from a given PDF.  For example, using a Markov-Chain Monte Carlo code such as `emcee` `[@emcee; @emceev3]`, the user has to provide both the initial positions in parameter space of each walker (often by drawing from a PDF) as well as a callable function which returns the log-likelihood, which in turn needs to include the log-probability of drawing each of the sampled values from the desired priors.  This generally requires manually creating or adjusting the callable function for any specific set of priors and sampled values, but is not convenient to do programatically.

`distl` is a Python package which allows for defining, combining, plotting, serializing, converting, exposing statistics, and sampling from complex probability distributions.  Whenever possible, the underlying distributions are handled by the appropriate functions in `scipy.stats` `[@scipy]`, with units support and conversion handled by `astropy.units` `[@astropy]`, and plotting support through `matplotlib` `[@matplotlib]` and `corner` `[@corner]`.  Additionally, `distl` adds support for "wrapping", including automatic wrapping when the units are angles (degrees will automatically wrap onto the $[0, 360]$ range, radians on $[0, 2\pi]$, etc.). Currently, `distl` includes support for the following distribution types as well as convenience functions to translate between them, wherever appropriate: delta, uniform (boxcar), gaussian (normal), histogram, samples (KDE representation of an existing set of samples from the distribution), function (custom callable function), multivariate gaussian, multivariate histogram, and multivariate samples.    

Additionally, these distribution types can be combined with any of the following math operations: addition, subtraction, multiplication, division, power, and, or, log, log10, as well as common trig operators (sin, cos, tan, arcsin, arccos, arctan, arctan2).  Whenever math operations are done between a distribution and an integer or float, the integer or float will be treated as a delta function at that value.  The resulting "composite" distribution stores references to the underlying distributions as well as the operator, allowing covariances of any underlying multivariate distributions to be maintained whenever possible.  For "and" operators, the PDFs of the two underlying distributions are sampled over their 99.99\% intervals and multiplied to create a new PDF.  A spline is then fit to the PDF and integrated to create the cummulative density function (CDF), which is then inverted to create the Point Probability Function (PPF).  These spline representations are then linearly interpolated to mimic the interface of any `scipy.stats` object. Because of this, the "and" operator cannot maintain underlying covariances.  Similarly, in the case of an "or" operator, the PDFs and CDFs of the two underlying distributions are sampled over their 99.9\% intervals and added to create the new PDFs and CDFs, respectively (and the CDF inverted to create the PPF function) and linearly interpolated to mimic a `scipy.stats` object.  As with "and" this ignored covariances.  When sampling, however, covariances can be maintained by instead randomly choosing which child distribution to sample
from and then sampling from that distribution directly.

As all these distribution objects can be serialized and deserialized and have a common interface for sampling and calculating probabilities, it becomes easy to generate these complex distributions and pass them through other codes flexibly.  For example, in the `emcee` case mentioned earlier, the log-probability function can remain fixed, only needing to loop over the provided set of priors and call the `logp` methods to account for the log-priors term in the log-likelihood.

`distl` was designed to be used in `PHOEBE` `[@prsa2016; @horvat2018; @jones2020]` - a software package to model eclipse binaries - as part of a release to support solving the inverse problem with optimizers and samplers (including `emcee`).  With `distl`, `PHOEBE` now allows the user to easily define and manipulate distributions, provide priors to the merit function,  process results from samplers into multivariate posterior distributions, and propagate any set of distributions through the forward model.

`distl` is hosted at the [GitHub repository](https://github.com/kecnry/distl), with documentation at [distl.readthedocs.io](https://distl.readthedocs.io), and is available for installation via `pip install distl`.

# Acknowledgements

Thanks to many discussions and feedback from Andrej Prsa and Angela Kochoska.

# References
