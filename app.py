import logging
from logging.config import dictConfig

import yaml
from vyper import v

from providers.configuration_provider import get_domains
from schedulers.domain_update_scheduler import DomainUpdateScheduler
from schedulers.schedule_task_runner import ScheduledTasksRunner


def load_configs(configuration_files):
    v.automatic_env()
    v.set_env_key_replacer(".", "_")
    v.set_config_type("yaml")
    v.add_config_path("./resources/configurations")

    for configuration_file in configuration_files:
        v.set_config_name(configuration_file)
        v.merge_in_config()


def config_logger():
    with open('resources/log.yml', 'r') as f:
        config = yaml.safe_load(f.read())
        dictConfig(config)


def main():
    config_logger()
    load_configs([
        "cred",
        "general"
    ])

    logging.info("Started cloudflare-ddns application...")
    domain_update_scheduled_task = DomainUpdateScheduler()
    scheduler_runner = ScheduledTasksRunner()

    scheduler_runner.register(domain_update_scheduled_task)
    scheduler_runner.run_scheduler()


if __name__ == '__main__':
    main()
