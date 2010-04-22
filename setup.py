from setuptools import setup, find_packages

setup(
    name='django-post',
    version='dev',
    description='Django post app.',
    author='Praekelt Consulting',
    author_email='dev@praekelt.com',
    url='https://github.com/praekelt/django-post',
    packages = find_packages(),
    include_package_data=True,
)

