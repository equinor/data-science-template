import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name="example_datascience_project",
    # version="0.0.1",
    version_config={
      "version_format": "{tag}.dev{sha}",
      "starting_version": "0.0.1"
    },
    setup_requires=['better-setuptools-git-version'],
    author='Equinor ASA',
    author_email="Name@equinor.com",
    description="An example data science project",
    long_description=open('README.md').read(),
    packages=['examplepackage'],
    package_dir={'': 'src'},
    test_suite='tests',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ], install_requires=['numpy', 'pytest', 'pandas']
)
