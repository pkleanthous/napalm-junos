# -*- coding: utf-8 -*-
import yaml
import jinja2
import difflib
import os
import shutil
import time


def diff(templates_path, template_file, confg_file, expected_config):

    start_timestamp = time.time()

    ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(
        templates_path))

    if not os.path.exists(".jinja2_unit_testing"):
        os.mkdir(".jinja2_unit_testing", 0755)

    with open(confg_file) as config:
        config = yaml.load(config)

    template = ENV.get_template(template_file)
    output = template.render(config)

    f = open('.jinja2_unit_testing/.tmpfile', 'w')
    f.write(output)
    f.close()

    file1 = open(".jinja2_unit_testing/.tmpfile", "r")
    file2 = open(expected_config, "r")

    diff = difflib.ndiff(file2.readlines(), file1.readlines())

    for line in diff:
        if line.startswith('- '):
            line = line.strip('- ')
            print "Expected: %s" % line
        if line.startswith('+ '):
            line = line.strip('+ ')
            print "Got: %s" % line

    elapsed_time = time.time() - start_timestamp
    print "Elapsed Time: %.3f Seconds" % elapsed_time

    if os.path.exists(".jinja2_unit_testing"):
        shutil.rmtree(".jinja2_unit_testing")
