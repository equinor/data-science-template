try:
    from azureml.core import Run
except ImportError:
    pass


# access the Azure ML run
# init run param to check if running within AML
def get_AMLRun():
    """Try and get the Azure Machine Learning run

    Returns:
        Run: The Experiment run or None if no active run.
    """
    try:
        run = Run.get_context(allow_offline=False)
        return run
    except Exception as e:
        print("Caught = {}".format(e.message))
        return None
