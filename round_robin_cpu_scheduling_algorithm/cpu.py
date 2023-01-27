from .process import Process


class CPU:
    __cpu_status_choices = ['free', 'busy']

    def __init__(self):
        self._cpu_status = 'free'
        self._executing_process = None

    @property
    def executing_process(self):
        return self._executing_process

    @executing_process.setter
    def executing_process(self, process: [Process, None]):
        if isinstance(process, Process) or process is None:
            self._executing_process = process
            return
        raise ValueError('This object is not valid to execute on CPU.')

    @property
    def cpu_status(self):
        return self._cpu_status

    @cpu_status.setter
    def cpu_status(self, status):
        if status not in self.__cpu_status_choices:
            raise ValueError(f'Status {status} is not valid for CPU.')
        self._cpu_status = status

    def do_process(self, process):
        pass
