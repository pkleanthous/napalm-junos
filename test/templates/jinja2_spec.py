# -*- coding: utf-8 -*-
import yaml
import jinja2
import difflib
import os
import shutil
import time
import colorama


def diff(templates_path, template_file, confg_file, expected_config):

    start_timestamp = time.time()

    tmp_text = "\nRunning jinja2Spec...\n"
    print(colorama.Fore.GREEN + colorama.Style.NORMAL + tmp_text)

    tmp_text = "Template: %s Configuration file: %s Expected Configuration: %s\n" % (
        template_file, confg_file, expected_config)
    print(colorama.Fore.GREEN + colorama.Style.NORMAL + tmp_text)

    colorama.init()

    ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(
        templates_path))

    with open(confg_file) as config:
        config = yaml.load(config)

    template = ENV.get_template(template_file)
    output = template.render(config)

    tmp_list = []
    tmp_list = output.splitlines()
    tmp_list = [line for line in tmp_list if line.strip()]

    expected_cfg = open(expected_config, "r").readlines()

    lineNum = 0
    error_count = 0

    for expected_line in expected_cfg:
        expected_line = expected_line.strip('\n')
        if expected_line != tmp_list[lineNum]:
            tmp_text = "In Line: %d" % lineNum
            print(colorama.Fore.GREEN + colorama.Style.NORMAL + tmp_text)
            tmp_text = "Expected: %s" % expected_line
            print(colorama.Fore.GREEN + colorama.Style.NORMAL + tmp_text)
            tmp_text = "Got:      %s" % tmp_list[lineNum]
            print(colorama.Fore.RED + colorama.Style.NORMAL + tmp_text)
            error_count += 1
        lineNum += 1

    if error_count == 0:
        tmp_text = "You are awesome! jinja2 spec passed successfully"
        print(colorama.Fore.YELLOW + colorama.Style.NORMAL + tmp_text)
    else:
        tmp_text = "jinja2 spec found %d error(s)" % error_count
        print(colorama.Fore.RED + colorama.Style.BRIGHT + tmp_text)

    elapsed_time = time.time() - start_timestamp
    tmp_text = "Elapsed Time: %.3f Seconds\n" % elapsed_time
    print(colorama.Fore.GREEN + colorama.Style.NORMAL + tmp_text)
