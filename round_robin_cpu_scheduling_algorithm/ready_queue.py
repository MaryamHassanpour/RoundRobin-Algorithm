import logging

from .process import Process

logger = logging.getLogger(__name__)


class ReadyQueue:
    def __init__(self):
        self._queue = []

    def enqueue(self, process: Process):
        if isinstance(process, Process):
            self._queue.append(process)
            print(f'process with id {process.id} inserted to ready queue.')
        else:
            logger.error('This process object is not valid to insert in ready queue.')

    def dequeue(self):
        try:
            return self._queue.pop(0)
        except IndexError:
            logger.error('Queue is empty.')

    @property
    def queue_length(self):
        return len(self._queue)
