import logging

from requests import get


class IpProvider:

    def __init__(self):
        self.cached_ip = None

    def check_ip(self):
        ip = get('https://api.ipify.org').text
        logging.info(f"Your ip is {ip}")
        if self.cached_ip is None or self.cached_ip != ip:
            self.cached_ip = ip
            return ip, True
        return self.cached_ip, False
