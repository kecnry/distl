```python
import distl
```


```python
out = (distl.uniform(-10,10) | distl.gaussian(0, 3) | distl.uniform(-3,3).scale_vert(0.5)).plot_pdf(show=True)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    ~/.local/lib/python3.7/site-packages/distl-0.1.0.dev0-py3.7.egg/distl/distl.py in __getattr__(self, name)
        323             try:
    --> 324                 return super(BaseDistribution, self).__getattr__(name)
        325             except:


    AttributeError: 'super' object has no attribute '__getattr__'

    
    During handling of the above exception, another exception occurred:


    AttributeError                            Traceback (most recent call last)

    <ipython-input-18-e05c6eb72de6> in <module>
    ----> 1 out = (distl.uniform(-10,10) | distl.gaussian(0, 3) | distl.uniform(-3,3).scale_vert(0.5)).plot_pdf(show=True)
    

    ~/.local/lib/python3.7/site-packages/distl-0.1.0.dev0-py3.7.egg/distl/distl.py in __getattr__(self, name)
        324                 return super(BaseDistribution, self).__getattr__(name)
        325             except:
    --> 326                 raise AttributeError("{} does not have attribute {}".format(self.__class__.__name__.lower(), name))
        327 
        328     def __setattr__(self, name, value):


    AttributeError: uniform does not have attribute scale_vert



```python

```
