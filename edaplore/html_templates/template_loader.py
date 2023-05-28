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

    # Create the absolute path to the 'html_templates' directory
    result_path = os.path.join(relative_path, "html_templates")

    # Create the Jinja2 environment with the 'html_templates' directory as the loader
    env = Environment(loader=FileSystemLoader(result_path))

    # Get the template with the given name
    template = env.get_template(tmp)

    # Return the template
    return template
