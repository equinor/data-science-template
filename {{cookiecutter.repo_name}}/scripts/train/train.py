#!/usr/bin/env python

"""Train a model.

Argv:
    output-dir: A folder to store any output to
    kernel: Kernel type to be used in the algorithm
    penalty: Penalty parameter of the error term
"""
import argparse
import joblib
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

from sklearn import datasets
from sklearn.metrics import classification_report
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.svm import SVC

from amlrun import get_AMLRun


def train(output_dir='outputs', kernel='linear', penalty=1.0):
    # make sure output directory exist
    os.makedirs(output_dir, exist_ok=True)

    # Safely get the Azure ML run
    run = get_AMLRun()

    # loading the iris dataset
    iris = datasets.load_iris()

    # X -> features, y -> label
    X = iris.data
    y = iris.target
    class_names = iris.target_names

    # dividing X, y into train and test data. Random seed for reproducability
    X_train, X_test, y_train, y_test = \
        train_test_split(X, y, test_size=0.20, random_state=0)

    # create our model - a linear SVM classifier
    svm_model_linear = SVC(kernel=kernel, C=penalty)

    # evaluate each model in turn
    kfold = StratifiedKFold(n_splits=10, random_state=1)
    cv_results = cross_val_score(svm_model_linear, X_train, y_train,
                                 cv=kfold, scoring='accuracy')

    print('Cross Validation Mean: ', cv_results.mean())
    print('Cross Validation Std: ', cv_results.std())
    if run is not None:
        run.log_list('Cross Validation Accuracies', cv_results)
        run.log('Cross Validation Mean', cv_results.mean())
        run.log('Cross Validation Std', cv_results.std())

    # now training on the full dataset
    svm_model_linear.fit(X_train, y_train)
    y_pred = svm_model_linear.predict(X_test)

    # model accuracy for X_test
    accuracy = svm_model_linear.score(X_test, y_test)
    print('Accuracy of SVM classifier on test set: {:.2f}'.format(accuracy))
    if run is not None:
        run.log('Accuracy', np.float(accuracy))

    # Plot non-normalized confusion matrix
    title = 'Test confusion matrix'
    disp = plot_confusion_matrix(svm_model_linear, X_test, y_test,
                                 display_labels=class_names,
                                 cmap=plt.cm.Blues)
    disp.ax_.set_title(title)
    print(title)
    print(disp.confusion_matrix)

    if run is not None:
        run.log_image(title, plot=plt)
    else:
        plt.savefig(os.path.join(output_dir, 'confusion_matrix.png'))

    # Plot normalized confusion matrix
    title = 'Normalized test confusion matrix'
    disp = plot_confusion_matrix(svm_model_linear, X_test, y_test,
                                 display_labels=class_names,
                                 cmap=plt.cm.Blues,
                                 normalize='true')
    disp.ax_.set_title(title)
    print(title)
    print(disp.confusion_matrix)

    if run is not None:
        run.log_image(title,  plot=plt)
    else:
        plt.savefig(
            os.path.join(output_dir, 'confusion_matrix_normalised.png'))

    # Print classification report
    print(classification_report(y_test, y_pred))

    # files saved in the "outputs" folder are automatically uploaded into
    # Azure ML Service run history
    model_folder = os.path.join(output_dir, 'model')
    model_path = os.path.join(model_folder, '{{cookiecutter.mlops_name}}.joblib')
    os.makedirs(model_folder, exist_ok=True)
    joblib.dump(svm_model_linear, model_path)
    print('Output saved to', output_dir)


def main(arguments):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # environment parameters
    # parser.add_argument(
    #     '--data-folder',
    #     help="local path to training data",
    #     required=True
    # )

    parser.add_argument(
        "--output-dir", type=str,
        default=os.path.join('..', '..', 'data', 'training', 'outputs'),
        help='location to write output'
    )

    # training specific parameters
    parser.add_argument('--kernel', type=str, default='linear',
                        help='Kernel type to be used in the algorithm')
    parser.add_argument('--penalty', type=float, default=1.0,
                        help='Penalty parameter of the error term')

    # parse the arguments
    args = parser.parse_args(arguments)

    # setup output directory
    # model_output_dir = os.path.join(
    #     os.path.dirname(os.path.realpath(__file__)),
    #     args.output_dir)
    # os.makedirs(args.output-dir, exist_ok=True)

    train(args.output_dir, args.kernel, args.penalty)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
