import logging

import CloudFlare
from schedule import Scheduler
from providers.configuration_provider import get_domains, get_credential
from providers.ip_provider import IpProvider


class DomainUpdateScheduler(Scheduler):

    def __init__(self):
        self.ip_provider = IpProvider()

    def execute(self):
        try:
            domains = get_domains()
            current_ip, is_new_ip = self.ip_provider.check_ip()

            if is_new_ip:
                for domain in domains:
                    self.update_a_records(domain.strip(), current_ip)
            else:
                logging.info("IP didn't change")
        except Exception as error:
            logging.exception("Error while updating domains A records: %s", error)

    def update_a_records(self, domain_name, new_ip):
        api, email = get_credential()
        cf = CloudFlare.CloudFlare(token=api, email=email)
        zone = cf.zones.get(params={"name": domain_name})
        if len(zone) > 0:
            dns_records = cf.zones.dns_records.get(zone[0]['id'], params={"type": "A"})
            for dns_record in dns_records:
                if dns_record['content'] != new_ip:
                    cf.zones.dns_records.put(zone[0]['id'],
                                             dns_record['id'],
                                             data={
                                                 "content": new_ip,
                                                 'type': dns_record['type'],
                                                 'name': dns_record['name']
                                             })
                    logging.info("Finished update record %s with ip %s", dns_record['name'], new_ip)
                else:
                    logging.info("No need to update record %s, because IP is the same", dns_record['name'])
