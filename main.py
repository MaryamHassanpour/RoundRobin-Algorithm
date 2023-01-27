from round_robin_cpu_scheduling_algorithm.cpu import CPU
from round_robin_cpu_scheduling_algorithm.cpu_scheduler import CPUScheduler
from round_robin_cpu_scheduling_algorithm.process import Process
from round_robin_cpu_scheduling_algorithm.ready_queue import ReadyQueue

if __name__ == '__main__':
    cpu = CPU()
    ready_queue = ReadyQueue()

    process_numbers = int(input('Enter total number of processes: '))

    for i in range(1, process_numbers + 1):
        cpu_burst_time = int(input(f'Enter process P{i} burst time: '))
        ready_queue.enqueue(Process(cpu_burst_time))

    time_quantum = int(input('Enter time quantum: '))

    cpu_scheduler = CPUScheduler(time_quantum, cpu, ready_queue)
    cpu_scheduler.schedule()
