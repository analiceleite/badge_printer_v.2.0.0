import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
django.setup()

from django.contrib.auth.models import User

user = User.objects.create_user(username='92903630', password='password', first_name="John", email="joao.ano03@gmail.com")
