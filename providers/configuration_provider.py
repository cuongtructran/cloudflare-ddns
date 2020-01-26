import yaml


def get_domains():
    with open('resources/configurations/general.yaml') as f:
        return yaml.load(f, Loader=yaml.FullLoader).get('domains')


def get_interval():
    with open('resources/configurations/general.yaml') as f:
        return yaml.load(f, Loader=yaml.FullLoader).get('check_interval')
