import os
import subprocess
import tempfile
import nbformat

import numpy as np


def run_notebook(filename):
    """
    Execute the specified notebook via jupyter nbconvert and collect output.
    :returns (parsed nb object, execution errors)
    """
    os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    # get temporary file ( and then close to avoid multiple write problems
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        temp_name = fout.name

    # run jupyter nbconvert
    args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
            "--ExecutePreprocessor.timeout=60", "--output", fout.name, filename]
    subprocess.check_call(args, shell=True)

    # read and parse notebook
    with open(temp_name, "r") as fout:
        fout.seek(0)
        nb = nbformat.read(fout, nbformat.current_nbformat)

    errors = [output for cell in nb.cells if "outputs" in cell
              for output in cell["outputs"] \
              if output.output_type == "error"]

    return nb, errors


# Commented out for now pending an update to automatically set the conda environment.
# This will work, but only if all libraries are in your default python environment. As I am using miniconda and the
# example notebook uses numpy from within a separate environment this doesn't work for me.
#def test_notebook():
#    nb, errors = run_notebook('notebooks\example.ipynb')
#    assert errors == []
