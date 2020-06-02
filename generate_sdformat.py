#!/usr/bin/env python3
from jinja2 import Environment, FileSystemLoader

"""
Compile SDFormat templates into SDFormat robot description
"""

loader = FileSystemLoader(searchpath="./src/")
env = Environment(loader=loader)

# Load and compile Jinja2 template
template = env.get_template("kraby.sdf.j2")
with open("hexapod.sdf", "w") as f:
    f.write(template.render())

