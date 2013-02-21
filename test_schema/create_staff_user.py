from customer.models import Client
from django.db import connection
from django.contrib.auth.models import User

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

#Selects tenant1 scheme
tenant1 = Client.objects.get(schema_name='tenant1')
connection.set_tenant(tenant1)

#creates staff user in scheme tenant1
myuser = User.objects.create_user('myuser','myuser@example.com','password')
myuser.is_staff = True
myuser.save()

#creates permissions for adding a post
content_type = ContentType.objects.get(app_label='test_app', model='post')
permission = Permission.objects.create(codename='can_publish',name='Can Publish Posts',content_type=content_type)

#gets a permission for a model adds permission and saves to user
permission = Permission.objects.get(codename='add_post')
myuser.user_permissions.add(permission)
permission = Permission.objects.get(codename='change_post')
myuser.user_permissions.add(permission)
permission = Permission.objects.get(codename='delete_post')
myuser.user_permissions.add(permission)

myuser.save()
