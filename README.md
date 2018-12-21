[![](https://travis-ci.org/Statoil/data-science-template.svg?branch=master)](https://travis-ci.org/Statoil/data-science-template?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/Statoil/data-science-template/badge.svg?branch=master)](https://coveralls.io/github/Statoil/data-science-template?branch=master)

# Data Science Template
This is a simple starting template for data science projects. It contains many of the essential artifacts that you will
need and presents a number of best practices including a standard template to guide and gather information relating to 
the process and specific use case. 

As it is impossible to create a single template that will meet every projects needs, this example should be considered
a starting point and changed based upon the working and evolution of your project.

Before working with the contents of this template or Data Science projects in general it is recommended to familiarise yourself with the Equinor [Data Science Technical Standards](https://wiki.statoil.no/wiki/index.php/Statoil_Data_Science_Technical_Standards) (Equinor internal only)

## Getting Started With This Template
This git repository contains only this template which is a starting point for your own work. You will need to create your own project specific repository to which you should copy the contents of this template. You can do this manually by download a zipped copy of the files using the "Clone or download" button or with the following commands (substitute myproject with the name of your project and REMOTE-REPOSITORY-URL with the remote repository url).

```
git clone https://github.com/Statoil/data-science-template myproject
cd myproject
rm -rf .git<br/>
git init<br/>
git add .<br/>
git commit -m "Initial commit"<br/>
git remote add origin REMOTE-REPOSITORY-URL<br/>
git remote -v<br/>
git push origin master<br/>
```

You should then modify the contents of your new copy as suited (alternatively before adding hte files to git). In particular you might want to do the following:

* Update this readme file to describe your project including setup, configuration and usage. You might also delete this Getting Started section once you have considered the steps below
* If using Travis for CI then modify .travis.yml as needed, if not then delete this file / replace with another for e.g. Jenkins. 
* Change or delete the LICENSE file if your terms are different.
* Modify conda_env.yml with a project specific name
* Create a [requirements.txt](https://pip.pypa.io/en/stable/user_guide/) file for any non Conda packages.
* Rename src\examplepackage to something more relevant to your project (e.g. src\<projectname>). This will also require corresponding changes in:
   * tests\test_examplepackage_examplemodule.py - import statement 
   * notebooks\example.ipynb - import statement
   * setup.py - packages list

All changes should then be comitted to a new repository specific for your project. The setup steps below can then be run to configure the environment on yours, or someone elses computer.

The docs\process_documentation.md file should be completed phase by phase, and each phase result shall be submitted for review and approval before the project moves on to the next phase. This is to assist with the gathering of essential information required to deliver a correct and robust solution. The git respoitory shall be added to the script that populates the [knowledge repository](https://git.statoil.no/DataScience/projects) to ease future knowledge sharing.


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

6. .. Place your own project specific setup steps here e.g. copying data files ...

When distributing your module, you can create a Python egg with the command `python setup.py bdist_egg` and upload the egg.

NOTE: When working in the project notebooks from within the Equinor network, you may need to include the lines below if your proxy is not otherwise setup.

`os.environ['HTTP_PROXY']="http://www-proxy.statoil.no:80"`<br />
`os.environ['HTTPS_PROXY']="http://www-proxy.statoil.no:80"`

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
├── .gitignore               <- Files that should be ignored by git. Add seperate .gitignore files in sub folders if 
│                               needed
├── .travis.yml              <- Travis CI build file (used for validating this template). Internally we might use 
│                               Jenkins?
├── conda_env.yml            <- Conda environment definition for ensuring consistent setup across environments
├── LICENSE
├── README.md                <- The top-level README for developers using this project.
├── requirements.txt         <- The requirements file for reproducing the analysis environment, e.g.
│                               generated with `pip freeze > requirements.txt`. Might not be needed if using conda.
├── setup.py                 <- Metadata about your project for easy distribution.
│
├── data
│   ├── interim_[desc]       <- Interim files - give these folders whatever name makes sense.
│   ├── processed            <- The final, canonical data sets for modeling.
│   ├── raw                  <- The original, immutable data dump.
│   └── temp                 <- Temporary files.
│
├── docs                     <- Any specific documentation (try ideally to keep to README.md)
│   └── process_documentation.md  <- Standard template for documenting process and decisions.
│
├── examples                 <- Add folders as needed e.g. examples, eda, use case
│
├── extras                   <- Miscellaneous extras.
│   └── add_explorer_context_shortcuts.reg    <- Adds additional Windows Explorer context menus for starting jupyter.
│
├── notebooks                <- Notebooks for analysis and testing
│   ├── eda                  <- Notebooks for EDA
│   │   └── example.ipynb    <- Example python notebook
│   ├── features             <- Notebooks for generating and analysing features (1 per feature)
│   ├── modelling            <- Notebooks for modelling
│   └── preprocessing        <- Notebooks for Preprocessing 
│
├── reporting                <- Solutions for reporting of results
│   ├── webapp               <- Flask based template for displaying content including text and graphs
│   └── README.md            <- Information on usage and setup of the webapp sample and more
│
├── src                      <- Code for use in this project.
│   └── examplepackage       <- Example python package - place shared code in such a package
│       ├── __init__.py      <- Python package initialisation
│       ├── examplemodule.py <- Example module with functions and naming / commenting best practices
│       ├── features.py      <- Feature engineering functionality
│       ├── io.py            <- IO functionality
│       └── pipeline.py      <- Pipeline functionality
│
└── tests                    <- Test cases (named after module)
    ├── test_notebook.py     <- Example testing that Jupyter notebooks run without errors
    ├── examplepackage       <- examplepackage tests
        ├── examplemodule    <- examplemodule tests (1 file per method tested)
        ├── features         <- features tests
        ├── io               <- io tests
        └── pipeline         <- pipeline tests
```

## Testing
Reproducability and the correct functioning of code are essential to avoid wasted time. If a code block is copied more 
than once then it should be placed into a common script / module under src and unit tests added. The same applies for 
any other non trivial code to ensure the correct functioning.

To run tests, install pytest using pip or conda (should have been setup already if you used the conda_env.yml file) and 
then from the repository root run
 
```pytest```

## Contributing
Contributions to this template are greatly appreciated and encouraged.

To contribute an update simply:
* Create a new branch / fork for your updates.
* Check that your code follows the PEP8 guidelines (line lengths up to 120 are ok) and other general conventions within this document.
* Ensure that as far as possible there are unit tests covering the functionality of any new code.
* Check that all existing unit tests still pass.
* Edit this document if needed to describe new files or other important information.
* Create a pull request.

## Important Links
* https://wiki.statoil.no/wiki/index.php/Statoil_Data_Science_Technical_Standards - Data Science Technical Standards (Equinor Internal)
* https://dataplatformwiki.azurewebsites.net/doku.php - Data Platform wiki (Equinor internal)
* https://github.com/Statoil/data-science-shared - Shared Data Science Code Repository (Equinor internal)

## References
* https://github.com/Statoil/data-science-template/ - The master template for this project
* http://docs.python-guide.org/en/latest/writing/structure/
* https://github.com/Azure/Microsoft-TDSP
* https://drivendata.github.io/cookiecutter-data-science/

[//]: #
   [anaconda]: <https://www.continuum.io/downloads>
