{{cookiecutter.project_name}}
======================================================================

.. note::
   This documentation page is for your own use as you best see fit for your project.

   In some cases it might be enough with the README.md in the project root, however
   you might use this if you want to publish API documentation, or have a website
   where you want to make detailed project information available (you can e.g.
   publish direct from blob storage).

   To generate documentation install make and from the docs folder run:

      .. code-block::

         make html

   On Windows you can use the .bat file so from the docs folder just run:

      .. code-block::

         make html

Usage and setup
---------------

Information about this project including steps on how to setup, run examples
to reproduce results, and other guidelines.

.. note::
   Here you might include information about this project including steps on how to
   setup and reproduce results and findings, and other guidelines. As default we
   include the Equinor code of conduct, process documentation and any .rst files
   under the info folder. Edit / add / remove as needed. The table of contents is
   generated automatically based upon the referenced document headings.

.. toctree::
   :glob:
   :maxdepth: 2

   info/*

Results and findings
--------------------

Results and findings generated during the course of this project.

.. note::
   Here you might include a write up of results or links to notebooks or other
   information that contain results or other findings. As default we
   include any .rst files under the results folder. Edit / add / remove as needed.
   The table of contents is generated automatically based upon the referenced
   document headings.

.. toctree::
   :glob:
   :maxdepth: 2

   results/*

API Documentation
-----------------

Information on the underlying API including function, class and method
documentation.

.. note::
   If you don't want this, then your project probably isn't written according
   to best practices and likely not production ready. If you disagree, just
   edit and remove this section.

.. toctree::
   :maxdepth: 2

   api-{{cookiecutter.package_name}}

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
