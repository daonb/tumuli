# Tumului

This project is about collecting and RESTing a life's story
We use Python 3 and Django 2 and we're licensed under the 
BSD-license.

Contribuitions are welcomed and we try to keep things newbies friendly.  We need
content, issues, comments and pull requests.  If you're a coder, the best place
to start is our issues.  Please read them and help us shrpen them by commenting.

## Archritecure

A `biography` django application is wrapped in a tumuli project.
First 3 steps are models, admin-based interface and RESTFull API (based on DRF).
We probably need a `presentation` app as we don't want to clutter `biography`
with presentation data and it would be nice to support multiple presentations 
per biography.

## Installation

    $ pipenv --python 3.6
    $ pipenv install --dev
    $ pipenv shell
    $ ./manage.py check
    $ ./manage.py migrate
    $ ./manage.py runserver

and point your browser at http://localhost:8000

