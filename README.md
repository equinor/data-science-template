[![](https://travis-ci.org/Statoil/data-science-template.svg?branch=master)](https://travis-ci.org/Statoil/data-science-template?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/Statoil/data-science-template/badge.svg?branch=master)](https://coveralls.io/github/Statoil/data-science-template?branch=master)

# Data Science Template
This is a starter template for data science projects. It contains many of the essential artifacts that you will
need and presents a number of best practices including a standard template to guide and gather information relating to 
the process and specific use case. 

As it is impossible to create a single template that will meet every projects needs, this example should be considered
a starting point and changed based upon the working and evolution of your project.

Before working with the contents of this template or Data Science projects in general it is recommended to familiarise yourself with the Equinor [Data Science Technical Standards](https://wiki.statoil.no/wiki/index.php/Statoil_Data_Science_Technical_Standards) (Currently Equinor internal only)

## Getting Started With This Template
This template is provided as a [Cookiecutter template](http://cookiecutter.readthedocs.org/en/latest/installation.html) so you
can quickly create an instance customised for your project. An assumption is that you have a working python installation.

To get running, first install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher):

    pip install -U cookiecutter

Then generate a new project for your own use based upon the template, answering the questions to customise the generated 
project:

    cookiecutter https://github.com/equinor/data-science-template.git

*Getting problems? You can always download this repository using the download button and reference the local copy e.g. cookiecutter c:\Downloads\data-science-template, however ideally fix any git proxy or other issues that are causing problems.*

You are now ready to get started, however you should create a new github repository for your new project and add your 
project using the following commands (substitute myproject with the name of your project and REMOTE-REPOSITORY-URL 
with the remote repository url).

    cd myproject<
    git init<
    git add .
    git commit -m "Initial commit"
    git remote add origin REMOTE-REPOSITORY-URL
    git remote -v<
    git push origin master

Finally you may want to:

* Configure Azure DevOps for your new repository for CI / CD.
* Update the readme file with additional project specific details including setup, configuration and usage. 
* The docs\process_documentation.md file should be completed phase by phase, and each phase result shall be submitted for review and approval before the project moves on to the next phase. This is to assist with the gathering of essential information required to deliver a correct and robust solution. The git respoitory shall be added to the script that populates the [knowledge repository](https://git.statoil.no/DataScience/projects) to ease future knowledge sharing.

## Contributing to this template
Contributions to this template are greatly appreciated and encouraged.

To contribute an update simply:
* Create a new branch / fork for your updates.
* Check that your code follows the PEP8 guidelines (line lengths up to 120 are ok) and other general conventions within this document.
* Ensure that as far as possible there are unit tests covering the functionality of any new code.
* Check that all existing unit tests still pass.
* Edit this document if needed to describe new files or other important information.
* Create a pull request.

### Template development environment
To develop this template further you might want to setup a virtual environment

#### Setup using
```
cd data-science-template
python -m venv dst-env
```

#### Activate environment
Max / Linux
```
source dst-env/bin/activate
```

Windows
```
dst-env\Scripts\activate
```

#### Install Dependencies
```
pip install -r requirements.txt
```

    
#### Testing
To run the template tests, install pytest using pip or conda and then from the repository root run
 
    pytest tests

## Important Links
* https://wiki.statoil.no/wiki/index.php/Statoil_Data_Science_Technical_Standards - Data Science Technical Standards (Equinor Internal)
* https://dataplatformwiki.azurewebsites.net/doku.php - Data Platform wiki (Equinor internal)
* https://github.com/Statoil/data-science-shared - Shared Data Science Code Repository (Equinor internal)

## References
* https://github.com/Statoil/data-science-template/ - The master template for this project
* http://docs.python-guide.org/en/latest/writing/structure/
* https://github.com/Azure/Microsoft-TDSP
* https://drivendata.github.io/cookiecutter-data-science/
* https://github.com/audreyr/cookiecutter-pypackage

[//]: #
   [anaconda]: <https://www.continuum.io/downloads>
