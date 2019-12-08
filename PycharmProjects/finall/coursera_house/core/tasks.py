from __future__ import absolute_import, unicode_literals
from celery import task

from .models import Setting

@task()
def smart_home_manager():
    print(1)
    pass
