# Some original code Copyright (c) Audrey Roy Greenfeld and individual contributors -
# see https://github.com/audreyr/cookiecutter-pypackage/blob/master/LICENSE

from contextlib import contextmanager
import shlex
import os
import subprocess
import datetime
from cookiecutter.utils import rmtree


@contextmanager
def inside_dir(dir_path):
    """
    Execute code from inside the given directory
    :param dir_path: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dir_path)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


def run_inside_dir(command, dir_path):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dir_path: String, path of the directory the command is being run.
    """
    with inside_dir(dir_path):
        return subprocess.check_call(shlex.split(command))


def check_output_inside_dir(command, dir_path):
    """Run a command from inside a given directory, returning the command output"""
    with inside_dir(dir_path):
        return subprocess.check_output(shlex.split(command))


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_top_level_files = [f.basename for f in result.project.listdir()]
        assert '.gitignore' in found_top_level_files
        assert 'conda_env.yml' in found_top_level_files
        assert 'README.md' in found_top_level_files
        assert 'setup.py' in found_top_level_files

        assert os.path.isdir(os.path.join(result.project, 'src', 'project_name'))
        assert os.path.isdir(os.path.join(result.project, 'tests', 'project_name'))


def test_bake_and_run_tests(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert run_inside_dir('python setup.py pytest', str(result.project)) == 0
        print("test_bake_and_run_tests path", str(result.project))


def test_bake_selecting_license(cookies):
    license_strings = {
        'MIT': ('MIT ', 'MIT License', True),
        'LGPL3': ('GNU LESSER GENERAL PUBLIC LICENSE', 'GNU Lesser General Public License v3 (LGPLv3)', False),
        'GPL3': ('GNU GENERAL PUBLIC LICENSE', 'GNU General Public License v3 (GPLv3)', False)
    }
    for project_license, (license_subtext, setup_subtext, should_contain_year) in license_strings.items():
        with bake_in_temp_dir(cookies, extra_context={'open_source_license': project_license}) as result:
            license_file_path = result.project.join('LICENSE')
            print(license_file_path)
            assert license_subtext in license_file_path.read()
            if should_contain_year:
                now = datetime.datetime.now()
                assert str(now.year) in license_file_path.read()
            assert setup_subtext in result.project.join('setup.py').read()


def test_bake_not_open_source(cookies):
    with bake_in_temp_dir(cookies, extra_context={'open_source_license': 'Not open source'}) as result:
        found_top_level_files = [f.basename for f in result.project.listdir()]
        assert 'setup.py' in found_top_level_files
        assert 'LICENSE' not in found_top_level_files


def test_bake_package_name(cookies):
    with bake_in_temp_dir(cookies, extra_context={'package_name': 'my_package'}) as result:
        with inside_dir(result.project):
            assert os.path.isdir(os.path.join('src', 'my_package'))
            assert os.path.isdir(os.path.join('tests', 'my_package'))

            'from my_package import examplemodule' in \
                open(os.path.join('tests', 'my_package', 'examplemodule', 'test_add_value_to_numpy.py')).read()
            'from my_package import examplemodule' in \
                open(os.path.join('tests', 'my_package', 'examplemodule', 'test_hello_world.py')).read()
