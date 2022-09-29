import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_orm.settings')

import django
django.setup()

from testapp.models import Student
from random import *
from faker import Faker


fake=Faker()


