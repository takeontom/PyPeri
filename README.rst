===============================
PyPeri
===============================

PyPeri makes getting data out of Periscope easy, with a sane and understandable
API.

.. image:: https://img.shields.io/pypi/v/pyperi.svg
    :target: https://pypi.python.org/pypi/pyperi

.. image:: https://img.shields.io/travis/takeontom/PyPeri.svg
    :target: https://travis-ci.org/takeontom/pyperi

.. image:: https://readthedocs.org/projects/pyperi/badge/?version=latest
    :target: https://pyperi.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://pyup.io/repos/github/takeontom/pyperi/shield.svg
    :target: https://pyup.io/repos/github/takeontom/pyperi/
    :alt: Updates

.. image:: https://badge.waffle.io/takeontom/PyPeri.svg?label=ready&title=Ready
    :target: https://waffle.io/takeontom/PyPeri
    :alt: 'Stories in Ready'

* Free software: MIT license
* Documentation: https://pyperi.readthedocs.io.


Features
--------

* Python 3
* Easy to understand API
* Fully tested & documented

Functionality so far:

* Get information about Users
* Get information about Broadcasts
* Get a User's Broadcast history


About
-----

Periscope is pretty neat, but it's difficult to get information out of it in a
programatic way. Getting answers to simple questions like: "How many broadcasts
did our client do this week" is not trivial, and in-depth analysis is pretty
tough. This project is an attempt to make the lives of people who dip into
Digital Marketing a little better.

PyPeri attempts to do this by providing a sane interface, and hides some of the
tedium of using Periscope's API. For example, Periscope makes doing simple
things, like getting a list of a User's past Broadcasts a 2-step process:

1) Request a short-lived API session key from the Periscope Web Interface
2) Use the session key on the Periscope API Interface using the
   `getUserBroadcastsPublic` endpoint.

PyPeri simplifies this considerably::

    >>> from pyperi import Peri
    >>> pp = Peri()
    >>> history = pp.get_user_broadcast_history(username='george_clinton')


Quick start
-----------

Install via pip::

    $ pip install pyperi

Do stuff::

    >>> from pyperi import Peri
    >>> pp = Peri()
    >>> history = pp.get_user_broadcast_history(username='george_clinton')
    >>> print(history[0]['status'])
    #George Clinton listening to music in houston

Full documentation is available here: https://pyperi.readthedocs.io


License
-------

PyPeri is free software, distributed under the MIT license.
