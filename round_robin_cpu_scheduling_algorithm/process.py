import uuid
import logging

logger = logging.getLogger(__name__)


class Process:
    __process_status_choices = ['new', 'running', 'waiting', 'ready', 'terminated']

    def __init__(self, cpu_burst_time: int):
        self.id = uuid.uuid4().hex[:10]
        self._cpu_burst_time = cpu_burst_time
        self._remaining_time = cpu_burst_time
        self._process_status = 'new'

    @property
    def process_status(self):
        return self._process_status

    @process_status.setter
    def process_status(self, status: str):
        if status not in self.__process_status_choices:
            raise ValueError('This status is not valid for a process')
        self._process_status = status

    @property
    def remaining_time(self):
        return self._remaining_time

    @remaining_time.setter
    def remaining_time(self, _time: int):
        if not isinstance(_time, int) or _time < 0:
            raise ValueError('Remaining time value should be a positive integer.')
        self._remaining_time = _time
