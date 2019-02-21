## Function (class)


A Function distribution allows for any python callable to be stored that
utilizes distributions under-the-hood.  When calling [Function.sample](Function.sample.md),
any argument passed to the function that is a [BaseDistribution](BaseDistribution.md) object
will be sampled prior to being passed to the callable function.

In order to save or load these distributions, it is necessary to have
the `dill` package installed.  Note that you should not load from untrusted
sources, as any executable could be contained in the callable function.

See:

* [Function.to_dict](Function.to_dict.md)
* [Function.to_json](Function.to_json.md)
* [Function.to_file](Function.to_file.md)

for documentation on loading and saving Function distributions.



* [__init__](Function.__init__.md)
* [copy](Function.copy.md)
* [dist_args](Function.dist_args.md)
* [dist_func](Function.dist_func.md)
* [distribution](Function.distribution.md)
* [label](Function.label.md)
* [mean](Function.mean.md)
* [plot](Function.plot.md)
* [plot_dist](Function.plot_dist.md)
* [plot_gaussian](Function.plot_gaussian.md)
* [plot_sample](Function.plot_sample.md)
* [sample](Function.sample.md)
* [sample_args](Function.sample_args.md)
* [sample_func](Function.sample_func.md)
* [std](Function.std.md)
* [to](Function.to.md)
* [to_dict](Function.to_dict.md)
* [to_file](Function.to_file.md)
* [to_gaussian](Function.to_gaussian.md)
* [to_histogram](Function.to_histogram.md)
* [to_json](Function.to_json.md)
* [to_uniform](Function.to_uniform.md)
* [unit](Function.unit.md)
