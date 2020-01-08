[![Build Status](https://dev.azure.com/mhew/data-science-template/_apis/build/status/data-science-template?branchName=master)](https://dev.azure.com/mhew/data-science-template/_build/latest?definitionId=15&branchName=master)

# Data Science Template
This is a starter template for data science projects in Equinor, although it may also be useful for others. It contains many of the essential artifacts that you will need and presents a number of best practices including code setup, samples, MLOps using Azure, a standard document to guide and gather information relating to the data science process and more. 

As it is impossible to create a single template that will meet every projects needs, this example should be considered
a starting point and changed based upon the working and evolution of your project.

Before working with the contents of this template or Data Science projects in general it is recommended to familiarise yourself with the Equinor [Data Science Technical Standards](https://wiki.statoil.no/wiki/index.php/Statoil_Data_Science_Technical_Standards) (Currently Equinor internal only)

## Getting Started With This Template
This template is provided as a [Cookiecutter template](http://cookiecutter.readthedocs.org/en/latest/installation.html) so you
can quickly create an instance customised for your project. An assumption is that you have a working python installation.

To get running, first install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher):

    pip install -U cookiecutter

### Create project
Then generate a new project for your own use based upon the template, answering the questions to customise the generated 
project:

    cookiecutter https://github.com/equinor/data-science-template.git
    
The values you are prompted for are:

| Value                   | Description |
| :---                    | --- |
| project_name            | A name for your project. Used mostly within documentation | 
| project_description     | A description to include in the README.md | 
| repo_name               | The name of the github repository where the project will be held |
| conda_name              | The name of the conda environment to use |
| package_name            | A name for the generated python package. | 
| mlops_name              | Default name for Azure ML. | 
| mlops_compute_name      | Default Azure ML compute cluster name to use. | 
| author                  | The main author of the solution. Included in the setup.py file | 
| open_source_license     | What type of open source license the project will be released under | 
| devops_organisation     | An Azure DevOps organisation. Leave blank if you aren't using Azure DevOps | 

If you are uncertain about what to enter for any value then just accept the defaults. You can always change the generated project later.

*Getting problems? You can always download this repository using the download button above and reference the local copy e.g. cookiecutter c:\Downloads\data-science-template, however ideally fix any git proxy or other issues that are causing problems.*

You are now ready to get started, however you should first create a new github repository for your new project and add your 
project using the following commands (substitute myproject with the name of your project and REMOTE-REPOSITORY-URL 
with the remote repository url).

    cd myproject
    git init
    git add .
    git commit -m "Initial commit"
    git remote add origin REMOTE-REPOSITORY-URL
    git remote -v
    git push origin master

### Continuous Integration
Continuous Integration (CI) increase quality by building, running tests and performing other validation whenever 
code is committed. The template contains a build pipeline for Azure DevOps, however requires a couple of manual
steps to setup:

* Log in to http://dev.azure.com and browse to, or create an organisation & project. The project name should be the same as your github repository name.
* Under *Pipelines -> Builds select* *New Pipeline*
* Select github and then your repository. Login / grant any permissions as prompted
* In the review pane click *run*

You are now setup for CI and automated test / building. You should verify the badge link in this README corresponds 
with your DevOps project, and as a further step might setup any release pipelines for automated deployment.

At this stage the build pipeline doesn't include MLOps steps, although these can be added based uon your needs.

### Finally

* Update the project readme file with additional project specific details including setup, configuration and usage. 
* The docs\process_documentation.md file should be completed phase by phase, and each phase result shall be submitted for review and approval before the project moves on to the next phase. This is to assist with the gathering of essential information required to deliver a correct and robust solution. The git respoitory shall be added to the script that populates the [knowledge repository](https://git.statoil.no/DataScience/projects) to ease future knowledge sharing.

## Generated Project Contents
Depending upon the selected options when creating the project, the generated structure will look similar to the below:

```
├── .gitignore               <- Files that should be ignored by git. Add seperate .gitignore files in sub folders if 
│                               needed
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
│   ├── temp                 <- Temporary files.
│   └── training             <- Files relating to the training process
│
├── docs                     <- Documentation
│   ├── data_science_code_of_conduct.md  <- Code of conduct.
│   ├── process_documentation.md         <- Standard template for documenting process and decisions.
│   └── writeup              <- Sphinx project for project writeup including auto generated API.
│      ├── conf.py           <- Sphinx configurtation file.
│      ├── index.rst         <- Start page.
│      ├── make.bat          <- For generating documentation (Windows)
│      └── Makefikle         <- For generating documentation (make)
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
├── scripts                  <- Standalone scripts
│   ├── deploy               <- MLOps scripts for deployment (WIP)
│   │   └── score.py         <- Scoring script
│   ├── train                <- MLOps scripts for training
│   │   ├── submit-train.py  <- Script for submitting a training run to Azure ML Service
│   │   ├── submit-train-local.py <- Script for local training using Azure ML
│   │   └── train.py         <- Example training script using the iris dataset
│   ├── example.py           <- Example sctipt
│   └── MLOps.ipynb          <- End to end MLOps example (To be refactored into the above)
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

## Contributing to This Template
Contributions to this template are greatly appreciated and encouraged.

To contribute an update simply:
* Submit an issue describing your proposed change to the repo in question.
* The repo owner will respond to your issue promptly.
* Fork the desired repo, develop and test your code changes.
* Check that your code follows the PEP8 guidelines (line lengths up to 120 are ok) and other general conventions within this document.
* Ensure that your code adheres to the existing style. Refer to the
   [Google Cloud Platform Samples Style Guide](
   https://github.com/GoogleCloudPlatform/Template/wiki/style.html) for the
   recommended coding standards for this organization.
* Ensure that as far as possible there are unit tests covering the functionality of any new code.
* Check that all existing unit tests still pass.
* Edit this document and the template README.md if needed to describe new files or other important information.
* Submit a pull request.


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

#### Linting
To verify that your code adheres to python standards run linting as shown below:

    flake8 --max-line-length=120 *.py hooks/ tests/

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
