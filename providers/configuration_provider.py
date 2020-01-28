import yaml
from vyper import v


def get_domains():
    domains_string = v.get("domains")
    return domains_string.split(',')


def get_interval():
    return v.get_int("check_interval")


def get_credential():
    return v.get("cloudflare.apikey"), v.get("cloudflare.email")
