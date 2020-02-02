import logging

import re
from requests import get


class IpProvider:

    def __init__(self):
        self.cached_ip = None

    def check_ip(self):
        ip = get('https://api.ipify.org').text

        if not self.is_valid_ip(ip):
            raise Exception(f"Invalid IP returned from ipify: {ip}")

        logging.info(f"Your ip is {ip}")
        if self.cached_ip is None or self.cached_ip != ip:
            self.cached_ip = ip
            return ip, True
        return self.cached_ip, False

    def is_valid_ip(self, ip):
        found = re.fullmatch("\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}", ip)
        return found is not None
