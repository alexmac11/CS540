import random

class Process:
    def __init__(self, pid, tickets):
        #Initializes a process with a unique identifier and the number of lottery tickets it holds
        self.pid = pid
        self.tickets = tickets

class Scheduler:
    def __init__(self):
        #Initializes the Scheduler with an empty list to hold processes
        self.processes = []

    def add_process(self, process):
        #Adds a process to the list of processes
        self.processes.append(process)

    def allocate_tickets(self, pid, num_tickets):
        #Allocate additional lottery tickets to a specific process identified by pid
        for process in self.processes:
            if process.pid == pid:
                process.tickets += num_tickets
                break

    def select_next_process(self):
        #Select the next process to run based on the lottery scheduling algorithm
        total_tickets = sum(process.tickets for process in self.processes)
        winning_ticket = random.randint(1, total_tickets)
        current_ticket = 0

        for process in self.processes:
            current_ticket += process.tickets
            if current_ticket >= winning_ticket:
                return process.pid

if __name__ == "__main__":
    #Sample usage
    scheduler = Scheduler()

    #Adding processes
    scheduler.add_process(Process(1, 5))
    scheduler.add_process(Process(2, 3))
    scheduler.add_process(Process(3, 7))

    #Allocating tickets to processes
    scheduler.allocate_tickets(1, 2)
    scheduler.allocate_tickets(2, 1)
    scheduler.allocate_tickets(3, 3)

    #Selecting winner
    winner_pid = scheduler.select_next_process()
    print(f"Process {winner_pid} wins the lottery!")