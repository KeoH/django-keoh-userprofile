=====
Keoh User Profile
=====

Keoh User Profile is a very simple app to use extended version of Django
User model.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "user_profile" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'user_profile',
      )

2. Include the user_profile URLconf in your project urls.py like this::

      url(r'^profile/', include('user_profile.urls', namespace='profile')),

3. Run `python manage.py syncdb` to create the user-profile models.

4. Start the development server and visit http://127.0.0.1:8000,
   you need to create a superuser like this::

   	  python manage.py createsuperuser

5. Visit http://127.0.0.1:8000/admin to view the new app in Django Admin