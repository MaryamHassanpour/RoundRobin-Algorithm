import time

from .cpu import CPU
from .process import Process
from .ready_queue import ReadyQueue


class CPUScheduler:
    def __init__(self, time_quantum: float, cpu: CPU, ready_queue: ReadyQueue):
        self._time_quantum = time_quantum
        self._cpu = cpu
        self._ready_queue = ready_queue

    def schedule(self):
        while queue_len := self._ready_queue.queue_length:
            print('******************************')
            print(f'There are {queue_len} processes to schedule in ready queue.')
            cpu_status = self._cpu.cpu_status
            if cpu_status == 'free':
                process = self.choose_process_to_execute()
                print(
                    f'process {process.id} was chose by scheduler to execute on CPU.'
                )
                self.execute_process(process)
            else:
                pass

    def choose_process_to_execute(self):
        return self._ready_queue.dequeue()

    def execute_process(self, process):
        if self._time_quantum <= process.remaining_time:
            execution_time = self._time_quantum
        else:
            execution_time = process.remaining_time

        self._execute_process(process, execution_time)
        self.preempt_process()
        self.update_and_save_process_info(process, execution_time)

    def _execute_process(self, process, execution_time):
        self._allocate_cpu_to_process(process)
        start_time = time.time()
        print(f'CPU is allocated to process {process.id}.')

        while time.time() - start_time < execution_time:
            self._cpu.do_process(process)

        print(f'process {process.id} timed out after {execution_time} time units.')

    def _allocate_cpu_to_process(self, process):
        self._cpu.executing_process = process
        process.process_status = 'running'
        self._cpu.cpu_status = 'busy'

    def preempt_process(self):
        if self._cpu.cpu_status == 'free':
            raise 'CPU is free'
        self._cpu.executing_process = None
        self._cpu.cpu_status = 'free'
        print('process has preempted.')

    def update_and_save_process_info(self, process: Process, execution_time):
        self.decrease_remaining_time(process, execution_time)
        if process.remaining_time > 0:
            self._ready_queue.enqueue(process)
            process.process_status = 'ready'
        else:
            process.process_status = 'terminated'

    @staticmethod
    def decrease_remaining_time(process: Process, execution_time: float):
        process.remaining_time -= execution_time
