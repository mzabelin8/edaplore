import os
from pathlib import Path
from jinja2 import Environment, Template, FileSystemLoader, PackageLoader


def find_template(tmp):
    # Get the current working directory
    cwd = Path(os.getcwd())

    # Get the path to the 'myapp' directory

    myapp_dir = cwd
    while myapp_dir.name != 'hse2':
        myapp_dir = myapp_dir.parent

    # Get the relative path from the current working directory to 'myapp'
    relative_path = ''
    while cwd != myapp_dir:
        relative_path += '../'
        cwd = cwd.parent
    # relative_path = os.path.relpath(myapp_dir, cwd)
    result_path = os.path.join(relative_path, "html_templates")
    # return as string
    env = Environment(loader=FileSystemLoader(result_path))
    template = env.get_template(tmp)
    return template

