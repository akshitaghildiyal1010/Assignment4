class Process:
    def __init__(self, p_id, process_name, start_time, priority):
        self.p_id = p_id
        self.process_name = process_name
        self.start_time = start_time
        self.priority = priority

class ProcessTable:
    def __init__(self):
        self.processes = []

    def add_process(self, process):
        self.processes.append(process)

    def sort_by_p_id(self):
        self.processes.sort(key=lambda process: process.p_id)

    def sort_by_start_time(self):
        self.processes.sort(key=lambda process: process.start_time)

    def sort_by_priority(self):
        priority_order = {"Low": 1, "MID": 2, "High": 3}
        self.processes.sort(key=lambda process: priority_order[process.priority])

    def print_table(self):
        print("{:<5} {:<10} {:<15} {:<10}".format("P_ID", "Process", "Start Time", "Priority"))
        print("="*40)
        for process in self.processes:
            print("{:<5} {:<10} {:<15} {:<10}".format(process.p_id, process.process_name, process.start_time, process.priority))

if __name__ == "__main__":
    process_table = ProcessTable()

    process_table.add_process(Process("P1", "VSCode", 100, "MID"))
    process_table.add_process(Process("P23", "Eclipse", 234, "MID"))
    process_table.add_process(Process("P93", "Chrome", 189, "High"))
    process_table.add_process(Process("P42", "JDK", 9, "High"))
    process_table.add_process(Process("P9", "CMD", 7, "High"))
    process_table.add_process(Process("P87", "NotePad", 23, "Low"))

    print("Sorting Options:")
    print("1. Sort by P_ID")
    print("2. Sort by Start Time")
    print("3. Sort by Priority")

    option = int(input("Enter sorting option: "))

    if option == 1:
        process_table.sort_by_p_id()
    elif option == 2:
        process_table.sort_by_start_time()
    elif option == 3:
        process_table.sort_by_priority()
    else:
        print("Invalid option")

    process_table.print_table()