=====
Keoh User Profile
=====

Keoh User Profile is a very simple app to use extended version of Django
User model.

Quick start
-----------

1. Add "user_profile" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'user_profile',
      )

2. Run `python manage.py syncdb` to create the user-profile models::

	python manage.py syncdb

Or if you are using South, migrate:

	python manage.py migrate user_profile

3. Visit http://127.0.0.1:8000/admin to view the new app in Django Admin

Details
-----------

This application creates a user_profile table in your database, this model is linked to django user model,
you can access to avatar image through the userprofile object in the user instance object::

	user.userprofile.get_avatar()

It returns the complete url to the avatar file, or if it does not exist, it returns a default image.

Forms and user sign in and sign up
-----------

Documentation in progress.. :(
