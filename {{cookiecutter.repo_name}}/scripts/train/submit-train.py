#!/usr/bin/env python

"""Train a model remotely using Azure ML compute.

This will re-use the current python environment.

Argv:
    output-dir: A folder to store any output to
    kernel: Kernel type to be used in the algorithm
    penalty: Penalty parameter of the error term
"""
import argparse
import sys

import azureml.core
from azureml.core import Experiment, Workspace
from azureml.train.sklearn import SKLearn


def submit(experiment_name: str,
           compute_name: str,
           kernal: str,
           penalty: float):

    print("This notebook was created using version 1.0.83 of the Azure ML SDK")
    print("You are using version", azureml.core.VERSION, "of the SDK")

    # Get a reference to the workspace. Be sure to download the config.json
    # from your workspace and place in the parent folder.
    ws = Workspace.from_config()
    print('Loaded workspace', ws.name)

    # Reference the experiment
    experiment = Experiment(workspace=ws, name=experiment_name)
    print('Logging to experiment', experiment_name)

    # Get a reference to an existing the compute target.
    compute_target = ws.compute_targets[compute_name]

    # Setup an Estimator for submitting the job. An Estimator further wraps
    # RunConfig with additional configuration for specific cases. There are
    # Estimators provided for many common runtimes such as PyTorch and
    # Tensorflow. In this case we use the SKLearn specific estimator.
    script_params = {
        '--output-dir': "outputs",
        '--kernel': kernal,
        '--penalty': penalty,
    }

    # NOTE: scikit-learn added below until default image includes v22.1+
    estimator = SKLearn(source_directory=".",
                        entry_script='train.py',
                        script_params=script_params,
                        compute_target=compute_target,
                        pip_packages=['matplotlib', 'scikit-learn'])

    # Submit the experiment to get a run and wait for completion
    run = experiment.submit(estimator)
    print('Submitted please wait...')
    run.wait_for_completion(show_output=True)

    # register the trained model
    model = run.register_model(
        model_name='{{cookiecutter.mlops_name}}',
        model_path='outputs/model/{{cookiecutter.mlops_name}}.joblib')

    print('Run number:', run.number)
    print('Run id:', run.id)
    print("Run details are available at:", run.get_portal_url())
    print("Model: {} v{}".format(model.name, model.version))

    if 'azureml.git.dirty' in run.properties:
        if run.properties['azureml.git.dirty']:
            print("WARNNG: You have uncomitted changes. To ensure "
                  "reproducability check in your code before you train.")
    else:
        print('WARNNG: To ensure reproducability you should be using git!')


def main(arguments: list):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # environment parameters
    parser.add_argument('--experiment', type=str,
                        default='{{cookiecutter.mlops_name}}',
                        help='The name of the Azure ML Experiment')
    parser.add_argument('--compute-name', type=str,
                        default='{{cookiecutter.mlops_compute_name}}',
                        help='The name of the Azure ML compute cluster')

    # training specific parameters
    parser.add_argument('--kernel', type=str, default='linear',
                        help='Kernel type to be used in the algorithm')
    parser.add_argument('--penalty', type=float, default=1.0,
                        help='Penalty parameter of the error term')

    # parse the arguments
    args = parser.parse_args(arguments)

    # submit the job
    submit(args.experiment,
           args.compute_name,
           args.kernel,
           args.penalty)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
