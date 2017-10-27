![](https://travis-ci.org/Statoil/data-science-template.svg?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/Statoil/data-science-template/badge.svg?branch=master)](https://coveralls.io/github/Statoil/data-science-template?branch=master)

# DataScienceTemplate
This is a simple starting template for data science projects that contains many of the essential artifacts that you will need and presents a number of best practices.

As it is impossible to create a single template that will meet all of a projects needs this example should be considered dynamic and changed based upon the working and evolution of your project.

## Usage
Download a copy of the files from this repository and modify as suited. In particular this readme file should be 
updated to describe your project including setup, configuration and usage.If you clone the repository then be shore to 
commit to a new project specific repository. 

## Installation
1. Install git and checkout the [git code repository]
2. Install [anaconda] python version 3.6+
3. Change working directory into the git code repository root
4. Create the self contained conda environment. In a terminal go to the git code repository root and enter the command:

   `conda env create --file conda_env.yml`

5. Any python modules under src need to be available to other scripts. This can be done in a couple of ways. You can 
setup and install the python modules by executing the setup.py command below. 

   `python setup.py develop`
   
    As an alternative you may prefer to set the python path directly from notebooks, test scripts etc. From Pycharm 
    you can also right click the src folder and select the _Mark Directory As | Source Root_ option.



6. Further you should add project specific steps to this list e.g. copying data files...

## Using the Python environment

Once the Python environment has been set up, to use the environment you need to

* Activate the environment using the following command in a terminal window:
               * Windows: `activate my_environment`
               * Linux, OS X: `source activate my_environment`
               * The __environment is activated per terminal session__, so you must activate it every time you open terminal.


* Deactivate the environment using the following command in a terminal window:
               * Windows: `deactivate my_environment`
               * Linux, OS X: `source deactivate my_environment`
               
* To delete the environment use command (can't be undone):
    * `conda remove --name my_environment --all`

## Initial File Structure

```
├── .gitignore           <- Files that should be ignored by git. Add seperate .gitignore files in sub folders if needed
├── .travis.yml          <- Travis CI build file (used for validating this template). Internally we might use Jenkins?
├── environment.yml      <- conda environment definition for ensuring consistent setup across environments
├── LICENSE
├── README.md            <- The top-level README for developers using this project.
├── requirements.txt     <- The requirements file for reproducing the analysis environment, e.g.
│                           generated with `pip freeze > requirements.txt`
│
├── data
│   ├── interim_[desc]   <- Interim files - give these folders whatever name makes sense.
│   ├── processed        <- The final, canonical data sets for modeling.
│   └── raw              <- The original, immutable data dump.
│
├── docs                 <- Any specific documentation (try ideally to keep to README.md)
│
├── notebooks            <- Notebooks for EDA or otherwise.
│   └── example.ipynb    <- Example notebook
│
├── src                  <- Code for use in this project.
│   ├── python           <- Python modules can go under here
│   │   └── common       <- Folder for example common python functionality
│   │       ├── __init__.py  <- Python package directory
│   │       └── example.py   <- Example functions
│   │
│   ├── examples         <- Add folders as needed e.g. examples, eda, use case
│   │
│   └── tests            <- Test cases
│       ├── __init__.py
│       └── test_common_example.py     <- Example tests
```

## Testing
Reproducability and the correct functioning of code are essential to avoid wasted time. If a code block is copied more than one then it should be placed into a common script under src and unit tests added. The same applies for any other non trivial code to ensure the correct functioning.

To run tests, install pytest using pip or conda (should have been setup already if you used the conda_env.yml file) and 
then from the repository root run
 
```pytest```

[//]: #
   [anaconda]: <https://www.continuum.io/downloads>
