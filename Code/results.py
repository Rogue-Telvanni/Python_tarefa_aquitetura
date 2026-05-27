class Results:
    def __init__(self):
        # Change these to lists to hold the data for every single frame
        self.cpu_usage = []
        self.memory_usage = []
        self.time = []

    def add_data(self, cpu, memory, time_ms):
        self.cpu_usage.append(cpu)
        self.memory_usage.append(memory)
        self.time.append(time_ms)

    def print_averages(self, session_name):
        # Prevent division by zero if the loop closes instantly
        if len(self.time) == 0:
            return

        avg_cpu = sum(self.cpu_usage) / len(self.cpu_usage)
        avg_mem = sum(self.memory_usage) / len(self.memory_usage)
        avg_time = sum(self.time) / len(self.time)

        print(f"\n--- Final Averages ({session_name}) ---")
        print(f"Frames Processed: {len(self.time)}")
        print(f"Average Time:     {avg_time:.2f} ms")
        print(f"Average Memory:   {avg_mem:.2f} MB")
        print(f"Average CPU:      {avg_cpu:.2f} %")
        print("---------------------------------------\n")

        self.cpu_usage.clear()
        self.memory_usage.clear()
        self.time.clear()
