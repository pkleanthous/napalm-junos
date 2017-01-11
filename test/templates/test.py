import jinja2_spec

jinja2_spec.diff(templates_path='../../napalm_junos/templates',
                 template_file='set_hostname.j2',
                 confg_file='maroulla.yaml',
                 expected_config='set_hostname.expected')

jinja2_spec.diff(templates_path='../../napalm_junos/templates',
                 template_file='set_hostname.j2',
                 confg_file='maroulla.yaml',
                 expected_config='set_hostname_maroulla.expected')

jinja2_spec.diff(templates_path='../../napalm_junos/templates',
                 template_file='set_hostname.j2',
                 confg_file='example.yaml',
                 expected_config='set_hostname.expected')

jinja2_spec.diff(templates_path='../../napalm_junos/templates',
                 template_file='set_ntp_peers.j2',
                 confg_file='ntp_sample.yaml',
                 expected_config='ntp_sample.expected')

jinja2_spec.diff(templates_path='../../napalm_junos/templates',
                 template_file='set_ntp_peers.j2',
                 confg_file='ntp_sample.yaml',
                 expected_config='ntp_sample_1.expected')

jinja2_spec.diff(templates_path='../../napalm_junos/templates',
                 template_file='set_ntp_peers.j2',
                 confg_file='ntp_sample_1.yaml',
                 expected_config='ntp_sample_1.expected')

jinja2_spec.diff(templates_path='../../napalm_junos/templates',
                 template_file='set_ntp_peers.j2',
                 confg_file='ntp_sample_2.yaml',
                 expected_config='ntp_sample_2.expected')
