import logging

import CloudFlare
import yaml
from schedule import Scheduler
from providers.configuration_provider import get_domains, get_credential
from providers.ip_provider import IpProvider


class DomainUpdateScheduler(Scheduler):

    def __init__(self):
        self.ip_provider = IpProvider()

    def execute(self):
        domains = get_domains()
        current_ip, is_new_ip = self.ip_provider.check_ip()

        if is_new_ip:
            for domain in domains:
                self.update_a_records(domain.strip(), current_ip)
        else:
            logging.info("IP didn't change")

    def update_a_records(self, domain_name, new_ip):
        api, email = get_credential()
        cf = CloudFlare.CloudFlare(token=api, email=email)
        zone = cf.zones.get(params={"name": domain_name})
        if len(zone) > 0:
            a_records = cf.zones.dns_records.get(zone[0]['id'], params={"type": "A"})
            for a_record in a_records:
                if a_record['content'] != new_ip:
                    cf.zones.dns_records.post(a_record['id'], data={"content": new_ip})
                    logging.info("Finished update record %s with ip %s", a_record['name'], new_ip)
                else:
                    logging.info("No need to update record %s, because IP is the same", a_record['name'])
