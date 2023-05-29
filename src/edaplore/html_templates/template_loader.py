import os
from pathlib import Path
from jinja2 import Environment, Template, FileSystemLoader, PackageLoader


def find_template(tmp):

    # Create the Jinja2 environment with the 'html_templates' directory as the loader
    env = Environment(loader=FileSystemLoader('.'))

    # Get the template with the given name
    template = env.get_template(tmp)

    # Return the template
    return template
