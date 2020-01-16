from setuptools import setup, find_packages

setup(
    name='sqlalchemy_helper',
    version='0.1.0',
    packages=find_packages(),
    author='Jordan Hubscher',
    author_email='jordan.hubscher@gmail.com',
    description='Provides common utility functions and constants relevant to SQLAlchemy development.',
    keywords='python commons utility library',
    project_urls={'Source Code': 'https://github.com/jhubscher/sqlalchemy_helper'},
    install_requires=['SQLAlchemy', 'regex']
)
