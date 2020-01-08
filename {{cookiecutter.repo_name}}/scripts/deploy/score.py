#!/usr/bin/env python

"""Model scoring (WIP) - Contributions welcome!!
"""
# import argparse
import joblib
import json
import numpy

from azureml.core.model import Model

from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def init():
    global model
    model_path = Model.get_model_path('{{cookiecutter.mlops_name}}')
    # deserialize the model file back into a sklearn model
    model = joblib.load(model_path)


# note you can pass in multiple rows for scoring
def run(raw_data):
    try:
        data = json.loads(raw_data)['data']
        data = numpy.array(data)
        result = model.predict(data)
        # you can return any datatype if it is JSON-serializable
        return result.tolist()
    except Exception as e:
        error = str(e)
        return error


def main():
    # parser = argparse.ArgumentParser()
    # environment parameters
    # parser.add_argument(
    #     '--data-folder',
    #     help="local path to training data",
    #     required=True
    # )
    # parser.add_argument(
    #     "--output-dir", type=str, default=os.path.join('..', 'outputs'),
    #     help='location to writeoutput relative to this script'
    # )

    # parse the arguments
    # args = parser.parse_args()

    # ws = Workspace.from_config()
    # model = Model(ws, 'sklearn_mnist')

    # model.download(target_dir=os.getcwd(), exist_ok=True)

    # verify the downloaded model file
    file_path = "ml-service/{{cookiecutter.mlops_name}}.joblib"
    model = joblib.load(file_path)

    # loading the iris dataset
    iris = datasets.load_iris()

    # X -> features, y -> label
    X = iris.data
    y = iris.target

    # dividing X, y into train and test data
    _, X_test, _, y_test = train_test_split(X, y, random_state=0)

    # training a linear SVM classifier
    y_pred = model.predict(X_test)

    # model accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print('Accuracy of SVM classifier on test set: {:.2f}'.format(accuracy))


if __name__ == '__main__':
    main()
