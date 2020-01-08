#!/usr/bin/env python

"""Train a model locally using Azure ML.

This will re-use the current python environment.

Argv:
    output-dir: A folder to store any output to
    kernel: Kernel type to be used in the algorithm
    penalty: Penalty parameter of the error term
"""
import argparse
import sys

import azureml.core
from azureml.core import Experiment, ScriptRunConfig, Workspace


def submit(experiment_name: str,
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

    # Create the RunConfiguration that will be used
    arguments = [
        '--output-dir', "outputs",
        '--kernel', kernal,
        '--penalty', penalty,
    ]
    script_run_config = ScriptRunConfig(source_directory='.',
                                        script='train.py',
                                        arguments=arguments)

    # As we will run locally we can use our existing python environment
    script_run_config.run_config.environment. \
        python.user_managed_dependencies = True

    # Submit the experiment to get a run and wait for completion
    run = experiment.submit(script_run_config)
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
                        default='{{cookiecutter.mlops_name}}-local',
                        help='The name of the Azure ML Experiment')

    # training specific parameters
    parser.add_argument('--kernel', type=str, default='linear',
                        help='Kernel type to be used in the algorithm')
    parser.add_argument('--penalty', type=float, default=1.0,
                        help='Penalty parameter of the error term')

    # parse the arguments
    args = parser.parse_args(arguments)

    # submit the job
    submit(args.experiment,
           args.kernel,
           args.penalty)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
