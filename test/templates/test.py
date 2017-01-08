import jinja2_compare

jinja2_compare.diff(templates_path='../../napalm_junos/templates',
                    template_file='set_hostname.j2',
                    confg_file='maroulla.yaml',
                    expected_config='set_hostname.expected')

jinja2_compare.diff(templates_path='../../napalm_junos/templates',
                    template_file='set_hostname.j2',
                    confg_file='example.yaml',
                    expected_config='set_hostname.expected')
