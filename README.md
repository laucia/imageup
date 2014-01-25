=======
imageup
=======

Simple image uploader for Django : allow to upload images to the server and get its url without using a ftp.

Images can then by easily managed (ie: replaced or suppressed) from the django admin. 

Installation
============

- Put ``imageup`` in your ``INSTALLED_APPS``
- Synchronize this application to your database with ``syncdb`` or ``migrate`` if you are a South user.

Options:
- to personalize the name of the directory images are uploaded to, set ``IMAGEUP_MEDIA_FILENAME`` to the correct file in ``settings.py`` (default to ``'imageup'``)
