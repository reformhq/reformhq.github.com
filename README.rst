Jekyll-driven static site for reformhq.org
==========================================


Toolchain setup
---------------

https://github.com/mojombo/jekyll/wiki/install

- gem install jekyll
- pip install fabric


Preview
-------

::

    $ fab serve

Visit `<http://localhost:4000>`__ to preview.
Content will auto-regenerate upon file changes.


Publishing
----------

Github immediately publishes
the current contents of the ``master`` branch
using Jekyll.
