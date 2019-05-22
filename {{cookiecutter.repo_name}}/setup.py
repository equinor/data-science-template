import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()

{%- set license_classifiers = {
    'MIT': 'License :: OSI Approved :: MIT License',
    'LGPL3': 'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    'GPL3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(
    name="{{cookiecutter.project_name}}",
    # version="0.0.1",
    version_config={
      "version_format": "{tag}.dev{sha}",
      "starting_version": "0.0.1"
    },
    setup_requires=['pytest-runner', 'better-setuptools-git-version'],
    tests_require=['pytest', 'nbformat'],
    author='{{cookiecutter.author}}',
    author_email="Name@equinor.com",
    description="{{cookiecutter.project_description}}",
    long_description=open('README.md').read(),
    packages=['examplepackage'],
    package_dir={'': 'src'},
    test_suite='tests',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
    ], install_requires=['numpy', 'pytest', 'pandas']
)
