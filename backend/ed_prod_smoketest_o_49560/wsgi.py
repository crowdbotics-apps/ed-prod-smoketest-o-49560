"""
WSGI config for ed_prod_smoketest_o_49560 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "ed_prod_smoketest_o_49560.settings"
)

application = get_wsgi_application()
