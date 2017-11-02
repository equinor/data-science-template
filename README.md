![](https://travis-ci.org/Statoil/data-science-template.svg?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/Statoil/data-science-template/badge.svg?branch=master)](https://coveralls.io/github/Statoil/data-science-template?branch=master)

# DataScienceTemplate
This is a simple starting template for data science projects that contains many of the essential artifacts that you will
need and presents a number of best practices.

As it is impossible to create a single template that will meet all of a projects needs this example should be considered dynamic and changed based upon the working and evolution of your project.

## Usage
Download a copy of the files from this repository and modify as suited. In particular this readme file should be 
updated to describe your project including setup, configuration and usage.

You should commit all code changes to a new repository. All exploratory work should be kept and verified working as 
value is often produced in this part of an analysis, even if results disprove initial hypothesise. If working in a multi 
user team then a strategy for git branching and the use of merge requests should be agreed upon prior to startup.

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
   
    As an alternative you may prefer to set the python path directly from within notebooks, test scripts etc. From Pycharm 
    you can also right click the src folder and select the _Mark Directory As | Source Root_ option.

6. Further you should add your own project specific steps to this list e.g. copying data files...

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
├── notebooks            <- Notebooks for EDA or otherwise.
│   ├── example.ipynb    <- Example python notebook
│   └── example.rmd      <- Example R notebook
│
├── src                  <- Code for use in this project.
│   └── projectname      <- Example python module
│       ├── __init__.py  <- Python package directory
│       └── example.py   <- Example functions and naming / commenting best practices
│
└── tests                <- Test cases
    ├── test_notebook.py <- Example testing that Jupyter notebooks run without errors
    └── test_projectname_example.py     <- Example tests
```

## Testing
Reproducability and the correct functioning of code are essential to avoid wasted time. If a code block is copied more 
than once then it should be placed into a common script under src and unit tests added. The same applies for any other 
non trivial code to ensure the correct functioning.

To run tests, install pytest using pip or conda (should have been setup already if you used the conda_env.yml file) and 
then from the repository root run
 
```pytest```

## References
* http://docs.python-guide.org/en/latest/writing/structure/
* https://github.com/Azure/Microsoft-TDSP

[//]: #
   [anaconda]: <https://www.continuum.io/downloads>
