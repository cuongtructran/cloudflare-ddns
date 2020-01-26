import abc


class ScheduledTask(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def execute(self):
        pass
