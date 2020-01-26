import time

from providers.configuration_provider import get_interval
import schedule


class ScheduledTasksRunner:

    def __init__(self):
        self.tasks = []

    def register(self, scheduled_task):
        self.tasks.append(scheduled_task)

    def run_tasks(self):
        for task in self.tasks:
            task.execute()

    def run_scheduler(self):
        schedule.every(get_interval()).minutes.do(self.run_tasks)

        while True:
            schedule.run_pending()
            time.sleep(1)
