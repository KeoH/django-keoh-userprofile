# Keoh User Profile
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/KeoH/django-keoh-userprofile/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/KeoH/django-keoh-userprofile/?branch=master)

Keoh User Profile is a very simple app to use extended version of Django User model.

## Quick start


1. Add ```"user_profile"``` to your ```INSTALLED_APPS``` setting like this:
```
INSTALLED_APPS = (
    ...
    'user_profile',
)
```
2. Run migrate:
```
python manage.py migrate
```

## Details


This application creates a user_profile table in your database, this model is linked to django user model,
you can access to avatar image through the userprofile object in the user instance object:

```
user.userprofile.get_avatar()
```

It returns the complete url to the avatar file, or if it does not exist, it returns a default image.

## Forms and user sign in and sign up


Documentation in progress.. :(
