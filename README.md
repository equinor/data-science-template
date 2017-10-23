![](https://travis-ci.org/Statoil/data-science-template.svg?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/Statoil/data-science-template/badge.svg?branch=master)](https://coveralls.io/github/Statoil/data-science-template?branch=master)

# DataScienceTemplate
This is a simple starting template for data science projects that contains many of the essential artifacts that you will need and presents a number of best practices.

As it is impossible to create a single template that will meet all of a projects needs this example should be considered dynamic and changed based upon the working and evolution of your project.

# Usage
Download a copy of the files from this repository and modify as suited. In particular this readme file should be updated to describe your project including setup, configuration and usage.

# Initial File Structure

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
│   ├── __init__.py
│   ├── common           <- Folder for example common python functionality
│   │   ├── __init__.py
│   │   └── example.py   <- Example functions
│   │
│   └── tests            <- Test cases
│       ├── __init__.py
│       └── test_common_example.py     <- Example tests
```

# Testing
Reproducability and the correct functioning of code are essential to avoid wasted time. If a code block is copied more than one then it should be placed into a common script under src and unit tests added. The same applies for any other non trivial code to ensure the correct functioning.

To run tests, install pytest using pip or conda and then from the repository root run 
```pytest```
