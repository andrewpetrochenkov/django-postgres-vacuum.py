<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/django-postgres-vacuum.svg?maxAge=3600)](https://pypi.org/project/django-postgres-vacuum/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-postgres-vacuum.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-postgres-vacuum.py/actions)

### Installation
```bash
$ [sudo] pip install django-postgres-vacuum
```

##### `settings.py`
```python
INSTALLED_APPS+=['django_postgres_vacuum']
```

#### Examples
```python
from django.core.management import call_command

call_command('vacuum')
call_command('vacuum_full')
```

```bash
$ python manage.py vacuum
$ python manage.py vacuum_full
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
