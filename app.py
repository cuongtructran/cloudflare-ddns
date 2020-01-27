import logging.config

import yaml

from schedulers.domain_update_scheduler import DomainUpdateScheduler
from schedulers.schedule_task_runner import ScheduledTasksRunner


def config_logger():
    with open('resources/log.yml', 'r') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)


def main():
    config_logger()
    logging.info("Started cloudflare-ddns application...")
    domain_update_scheduled_task = DomainUpdateScheduler()
    scheduler_runner = ScheduledTasksRunner()

    scheduler_runner.register(domain_update_scheduled_task)
    scheduler_runner.run_scheduler()


if __name__ == '__main__':
    main()
