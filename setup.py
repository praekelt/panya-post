from setuptools import setup, find_packages

setup(
    name='django-post',
    version='dev',
    description='Django rich post app.',
    author='Shaun Sephton',
    author_email='shaunsephton@gmail.com',
    url='http://github.com/praekelt/django-post',
    packages = find_packages(),
    include_package_data=True,
)
