from codecs import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'VERSION'), encoding='utf-8') as f:
    version = f.read()


setup(
    name='django-keoh-userprofile',
    version=version,
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    include_package_data=True,
    description='A simple Django app to manage user profiles',
    long_description=long_description,
    url='https://github.com/KeoH/django-keoh-userprofile',
    author='Francisco Manzano Magaña',
    author_email='keoh77@gmail.com',
    install_requires=['pillow'],
    python_requires='>=3.4',
    keywords='profile,django,user',
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    project_urls={
        'Bug Reports': 'https://github.com/KeoH/django-keoh-userprofile/issues',  # noqa
        'Source': 'https://github.com/KeoH/django-keoh-userprofile/',
    }
)
