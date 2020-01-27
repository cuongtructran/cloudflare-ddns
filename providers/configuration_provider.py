import yaml


def get_domains():
    with open('resources/configurations/general.yml') as f:
        domains_string = yaml.load(f, Loader=yaml.FullLoader).get('domains')
        return domains_string.split(',')


def get_interval():
    with open('resources/configurations/general.yml') as f:
        return yaml.load(f, Loader=yaml.FullLoader).get('check_interval')
