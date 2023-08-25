class Process:
    def _init_(self, p_id, process_name, start_time, priority):
        self.p_id = p_id
        self.process_name = process_name
        self.start_time = start_time
        self.priority = priority

    def display(self):
        print(f"{self.p_id}\t{self.process_name}\t{self.start_time}\t{self.priority}")

class ProcessTable:
    def _init_(self):
        self.processes = []

    def add_process(self, process):
        self.processes.append(process)

    def sort_by_p_id(self):
        self.processes.sort(key=lambda process: process.p_id)

    def sort_by_start_time(self):
        self.processes.sort(key=lambda process: process.start_time)

    def sort_by_priority(self):
        self.processes.sort(key=lambda process: process.priority, reverse=True)

    def display_table(self):
        for process in self.processes:
            process.display()

def main():
    process_table = ProcessTable()

    # Sample data
    process_table.add_process(Process("P1", "VSCode", 100, "MID"))
    process_table.add_process(Process("P23", "Eclipse", 234, "MID"))
    process_table.add_process(Process("P93", "Chrome", 189, "High"))
    process_table.add_process(Process("P42", "JDK", 9, "High"))
    process_table.add_process(Process("P9", "CMD", 7, "High"))
    process_table.add_process(Process("P87", "NotePad", 23, "Low"))

    sorting_options = {
        1: process_table.sort_by_p_id,
        2: process_table.sort_by_start_time,
        3: process_table.sort_by_priority
    }

    print("Sorting Options:")
    print("1. Sort by P_ID")
    print("2. Sort by Start Time")
    print("3. Sort by Priority")

    choice = int(input("Enter your choice: "))

    if choice in sorting_options:
        sorting_options[choice]()
        process_table.display_table()
    else:
        print("Invalid choice!")

if _name_ == "_main_":
    main()