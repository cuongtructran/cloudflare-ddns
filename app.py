import logging

from schedulers.domain_update_scheduler import DomainUpdateScheduler
from schedulers.schedule_task_runner import ScheduledTasksRunner


def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting cloudflare-ddns application...")
    domain_update_scheduled_task = DomainUpdateScheduler()
    scheduler_runner = ScheduledTasksRunner()

    scheduler_runner.register(domain_update_scheduled_task)
    scheduler_runner.run_scheduler()


if __name__ == '__main__':
    main()
