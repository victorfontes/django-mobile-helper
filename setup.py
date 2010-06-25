#coding: utf-8
import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages
setup(
    name = "django-movel",
    version = "0.1",
    packages = find_packages(),
    author = "Victor Fontes",
    author_email = "contato@victorfontes.com",
    description = "A package to help dealing with mobile clients in Django",
    url = "http://github.com/victorfontes/django-mobile-helper",
    include_package_data = True
)