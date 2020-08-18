======
README
======

This application allows various webmaster tools to verify that a Django site is
managed by you.

The only supported method of verification is by accessing a file on your
server.

Supported services:

- `Google Webmaster Tools <https://www.google.com/webmasters/tools/home>`_
- `Bing Webmaster Tools <https://ssl.bing.com/webmaster/Home/>`_
- `Yandex Webmaster Tools <http://webmaster.yandex.com/>`_
- `Majestic SEO <https://www.majesticseo.com>`_
- `Alexa <http://www.alexa.com>`_

.. image:: https://api.travis-ci.org/nkuttler/django-webmaster-verification.png
  :target: https://travis-ci.org/nkuttler/django-webmaster-verification

Usage
=====

Get ``django-webmaster-verification`` into your python path::

    pip -m install git+git://github.com/ooppsss60/django-webmaster-verification

Add ``webmaster_verification`` to your INSTALLED_APPS in settings.py::

    INSTALLED_APPS = (
        ...,
        'webmaster_verification',
        ...,
    )

Add ``webmaster_verification`` to your root urlconf (urls.py)::

    urlpatterns = [
        ...,
        url(r'', include('webmaster_verification.urls')),
        ...,
    ]

Add verification codes in admin site: example.com/admin/webmaster_verification/verificationcode/

The codes are alphanumeric and don't include suffixes like 'html', e.g.
``847e1f379a99c28a`` for google, not ``847e1f379a99c28a.html``.

Multiple codes are supported as well, except for bing::

Notes
-----

As **Bing** always accesses the same verification file I'm not sure if it's
possible to support more than one code for it. Please let me know if yes, and
how, as I don't really use their tools.

For **Yandex** only the `.txt` file method is supported, but adding support for
`.html` should be trivial if you need it.

The **Alexa** codes I saw all had a length of 27 characters, so that's what this
app assumes is used. Please let me know if your codes differ and I need to
modify the app.
