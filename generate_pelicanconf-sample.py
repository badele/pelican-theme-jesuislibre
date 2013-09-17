#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# use:
# generate_pelicanconf-sample.py my_official_blog/pelicanconf.py | sort > pelicanconf-sample.py 

import sys
import imp
import os

from jinja2 import Environment, FileSystemLoader, meta


# Search all template files
def list_html_templates():
    dirList = os.listdir('templates')

    return dirList


# get all variable in template file
def get_variables(filename):
    env = Environment(loader=FileSystemLoader('templates'))
    template_source = env.loader.get_source(env, filename)[0]
    parsed_content = env.parse(template_source)

    return meta.find_undeclared_variables(parsed_content)


# Check if the pelicanconf is paseed
if len(sys.argv) != 2:
    print("Please indicate the pelicanconf.py file")
    sys.exit()

# Get all vars from templates files
all_vars = set()
files = list_html_templates()
for fname in files:
    variables = get_variables(fname)
    for var in variables:
        if var.isupper():
            all_vars.add(var)

m = imp.load_source('pelicanconf', sys.argv[1])

# Show pelicanconf.py vars content
for var in all_vars:
    varname = 'm.%s' % var
    if var in m.__dict__:
        print ("%s = %s" % (var, repr(m.__dict__[var])))
