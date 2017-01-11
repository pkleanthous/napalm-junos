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

    tmp_text = "Running jinja2Spec...\n"
    print(colorama.Fore.GREEN + colorama.Style.NORMAL +  tmp_text)

    tmp_text = "Template: %s Configuration file: %s Expected Configuration: %s\n" % (template_file, confg_file, expected_config)
    print(colorama.Fore.GREEN + colorama.Style.NORMAL +  tmp_text)

    colorama.init()

    ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(
        templates_path))

    if not os.path.exists(".jinja2_spec"):
        os.mkdir(".jinja2_spec", 0755)

    with open(confg_file) as config:
        config = yaml.load(config)

    template = ENV.get_template(template_file)
    output = template.render(config)

    f = open('.jinja2_spec/.tmpfile', 'w')
    f.write(output)
    f.close()

    generated_cfg = open(".jinja2_spec/.tmpfile", "r").readlines()
    expected_cfg = open(expected_config, "r").readlines()

    d = difflib.Differ()
    diffs = d.compare(expected_cfg, generated_cfg)
    lineNum = 0
    error_count = 0

    for line in diffs:
        opcode = line[:2]
        if opcode ==  "- ":
            expected_line = (line[2:].strip())
        if opcode in ("  ", "+ "):
            lineNum += 1
        if opcode == "+ ":
            tmp_text = "In Line: %d" % lineNum
            print(colorama.Fore.GREEN + colorama.Style.NORMAL +  tmp_text)
            tmp_text = "Expected: %s" % expected_line
            print(colorama.Fore.GREEN + colorama.Style.NORMAL + tmp_text)
            tmp_text = "Got:      %s" % (line[2:].strip())
            print(colorama.Fore.RED + colorama.Style.NORMAL + tmp_text)
            error_count += 1

    if error_count == 0:
        tmp_text = "You are awesome! jinja2 spec passed successfully"
        print(colorama.Fore.YELLOW + colorama.Style.NORMAL + tmp_text)
    else:
        tmp_text = "jinja2 spec found %d errors" % error_count
        print(colorama.Fore.RED + colorama.Style.BRIGHT + tmp_text)

    elapsed_time = time.time() - start_timestamp
    tmp_text = "Elapsed Time: %.3f Seconds\n" % elapsed_time
    print(colorama.Fore.GREEN + colorama.Style.NORMAL + tmp_text)

    if os.path.exists(".jinja2_spec"):
        shutil.rmtree(".jinja2_spec")
