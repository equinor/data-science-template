# import datetime
import os
# import shutil
# from os.path import join


def replace_contents(filename: str, what: str, replacement: str) -> None:
    """
    Replace instances of a given string in a file

    Args:
        filename: The filename to replace within
        what: The text that should be matched
        replacement: The text that what should be replaced with
    """
    with open(filename) as fh:
        changelog = fh.read()
    with open(filename, 'w') as fh:
        fh.write(changelog.replace(what, replacement))


if __name__ == "__main__":
    # today = datetime.date.today()
    # replace_contents('LICENSE', '<YEAR>', today.strftime("%Y"))

    if '{{ cookiecutter.open_source_license }}' == "Not open source":
        os.remove('LICENSE')
        # shutil.rmtree('LICENSE')

    # Print out some information on setup and next steps
    print("""

Data Science Project '{{ cookiecutter.repo_name }}' created using the following
parameters:

{% for key, value in cookiecutter.items()|sort %}
    {{ "{0:26}".format(key + ":") }} {{ "{0!r}".format(value).strip("u") }}
{%- endfor %}

You are now ready to get started, however you should create a new github
repository for your new project and add your project using the following
commands (substitute REMOTE-REPOSITORY-URL with the remote repository url).

    cd {{ cookiecutter.repo_name }}
    git init
    git add --all
    git commit -m "Initial commit"
    git remote add origin REMOTE-REPOSITORY-URL
    git push -u origin master
""")
