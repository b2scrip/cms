import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'prodct.settings'
django.setup()
from django.contrib.auth.models import User
