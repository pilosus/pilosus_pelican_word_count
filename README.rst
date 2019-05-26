`Pelican`_ plugin for word count and reading time statistics

About
-----

Words are extracted and refined from the rendered ``HTML``.

Reading time is in minutes and calculated assuming average reading
speed equal to ``250`` words per minute.


Installation
------------

1. Place plugin in a directory, e.g ``plugins/pilosus_pelican_word_count``.
   You can clone it or add it to your blog repo as a submodule:

.. code-block:: bash

  $ cd /path/to/your/static/site/repo
  $ git submodule add https://github.com/pilosus/pilosus_pelican_word_count plugins/pilosus_pelican_word_count


2. Add plugins configurations in a settings file:

.. code-block:: python

  PLUGIN_PATHS = ['plugins']
  PLUGINS = ['pilosus_pelican_word_count',]


Usage
-----

Plugin adds a ``stats`` attribute holding dictionary with article or
page statistics:

.. code-block:: python

  {
    'word_count': 500,
    'read_minutes': 2,
  }


In your template you can use it like this:

.. code-block:: jinja2

  {% if article and article.stats %}
  <span class="stats">article.stats['word_count'] words, article.stats['read_minutes'] minutes to read</span>
  {% endif %}

  {% if page and page.og %}
  <span class="stats">page.stats['word_count'] words, page.stats['read_minutes'] minutes to read</span>
  {% endif %}


License
-------

This work is licensed under GNU AFFERO GENERAL PUBLIC LICENSE Version 3.
See LICENSE file

.. _Pelican: https://docs.getpelican.com/en/stable/
