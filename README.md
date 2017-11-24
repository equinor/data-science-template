[![](https://travis-ci.org/Statoil/data-science-template.svg?branch=master)](https://travis-ci.org/Statoil/data-science-template?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/Statoil/data-science-template/badge.svg?branch=master)](https://coveralls.io/github/Statoil/data-science-template?branch=master)

# DataScienceTemplate
This is a simple starting template for data science projects. It contains many of the essential artifacts that you will
need and presents a number of best practices.

As it is impossible to create a single template that will meet every projects needs, this example should be considered
a starting point and changed based upon the working and evolution of your project.

## Getting Started
Make your own project specific copy of this repository by doing one of the following:

* Download a zipped copy of the files from the "Clone or download" button.
* Clone this repository, create a second copy locally from which you delete the .git folder or change the remotes. The expectation is that the contents will change so much as your analysis evolves that there is no point referring back to this original repository.

You should then modify the contents of your new copy as suited. In particular you might want to do the following:

* Update this readme file to describe your project including setup, configuration and usage. You might also delete this Getting Started section once you have considered the steps below
* Change or delete the LICENSE file if your terms are different.
* Modify conda_env.yml with a project specific name
* Rename src\examplepackage to something more relevant to your project (e.g. src\<projectname>). This will also require corresponding changes in:
   * tests\test_examplepackage_examplemodule.py - import statement 
   * notebooks\example.ipynb - import statement
   * setup.py - packages list

You should commit all code changes to a new repository. The setup steps below can then be run to configure the environment on yours, or someone elses computer.

## Setup
1. Install git and checkout the [git code repository]
2. Install [anaconda] python version 3.6+
3. Change working directory into the git code repository root
4. Create the self contained conda environment. In a terminal go to the git code repository root and enter the command:

   `conda env create --file conda_env.yml`

5. Any python modules under src need to be available to other scripts. This can be done in a couple of ways. You can 
setup and install the python modules by executing the setup.py command below which will install the packages to the 
conda environments site-packages folder but with a symlink to the src folder so modifications are reflected immediately. 

   `python setup.py develop`
   
    As an alternative you may prefer to set the python path directly from the console, within notebooks, test scripts 
    etc. From Pycharm you can also right click the src folder and select the _Mark Directory As | Source Root_ option.

6. Further you should edit this document to add your own project specific steps to this list e.g. copying data files...

## Using the Python Conda environment

Once the Python Conda environment has been set up, you can

* Activate the environment using the following command in a terminal window:

  * Windows: `activate my_environment`
  * Linux, OS X: `source activate my_environment`
  * The __environment is activated per terminal session__, so you must activate it every time you open terminal.

* Deactivate the environment using the following command in a terminal window:

  * Windows: `deactivate my_environment`
  * Linux, OS X: `source deactivate my_environment`
               
* Delete the environment using the command (can't be undone):

  * `conda remove --name my_environment --all`

## Initial File Structure

```
├── .gitignore           <- Files that should be ignored by git. Add seperate .gitignore files in sub folders if 
│                           needed
├── .travis.yml          <- Travis CI build file (used for validating this template). Internally we might use 
│                           Jenkins?
├── conda_env.yml        <- Conda environment definition for ensuring consistent setup across environments
├── LICENSE
├── README.md            <- The top-level README for developers using this project.
├── requirements.txt     <- The requirements file for reproducing the analysis environment, e.g.
│                           generated with `pip freeze > requirements.txt`. Might not be needed if using conda.
├── setup.py             <- Metadata about your project for easy distribution.
│
├── data
│   ├── interim_[desc]   <- Interim files - give these folders whatever name makes sense.
│   ├── processed        <- The final, canonical data sets for modeling.
│   └── raw              <- The original, immutable data dump.
│
├── docs                 <- Any specific documentation (try ideally to keep to README.md)
│
├── examples             <- Add folders as needed e.g. examples, eda, use case
│
├── extras               <- Miscellaneous extras.
│   └── add_explorer_context_shortcuts.reg    <- Adds additional Windows Explorer context menus for starting jupyter.
│
├── notebooks            <- Notebooks for EDA or otherwise.
│   ├── example.ipynb    <- Example python notebook
│   └── example.rmd      <- Example R notebook
│
├── src                  <- Code for use in this project.
│   └── examplepackage   <- Example python package - place shared code in such a package
│       ├── __init__.py  <- Python package initialisation
│       └── examplemodule.py  <- Example module with functions and naming / commenting best practices
│
└── tests                <- Test cases
    ├── test_notebook.py <- Example testing that Jupyter notebooks run without errors
    └── test_examplemodule_examplemodule.py     <- Example tests
```

# Some Guidelines
The following are some guidelines for usage and working together. Expand upon this list as needed.

* All exploratory work should be kept and verified working, as value is often produced in this part of an analysis, even if results disprove initial hypothesise. 
* If working in a multi user team then a strategy for git branching and the use of merge requests should be agreed upon prior to startup.

## Testing
Reproducability and the correct functioning of code are essential to avoid wasted time. If a code block is copied more 
than once then it should be placed into a common script / module under src and unit tests added. The same applies for 
any other non trivial code to ensure the correct functioning.

To run tests, install pytest using pip or conda (should have been setup already if you used the conda_env.yml file) and 
then from the repository root run
 
```pytest```

## Important Links
* https://dataplatformwiki.azurewebsites.net/doku.php - Data Platform wiki

## References
* https://github.com/Statoil/data-science-template/ - The master template for this project
* http://docs.python-guide.org/en/latest/writing/structure/
* https://github.com/Azure/Microsoft-TDSP
* https://drivendata.github.io/cookiecutter-data-science/

[//]: #
   [anaconda]: <https://www.continuum.io/downloads>
