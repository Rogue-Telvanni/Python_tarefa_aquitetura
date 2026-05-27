import time
import psutil
import tracemalloc
import statistics
import os
import primes  # Your prime generator file

def benchmark_function(name, func, *args, iterations=20):
    times = []
    process = psutil.Process(os.getpid())

    process.cpu_percent(interval=None)
    tracemalloc.start()

    for _ in range(iterations):
        start_time = time.perf_counter()

        result = func(*args)

        # force genrator to a list
        if hasattr(result, '__iter__') and not isinstance(result, (list, tuple, dict, str)):
            list(result)

        end_time = time.perf_counter()
        times.append((end_time - start_time) * 1000)  # Convert to milliseconds

    _, peak_memory_bytes = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    cpu_usage = process.cpu_percent(interval=None)

    return {
        "Method": name,
        "Mean": statistics.mean(times),
        "StdDev": statistics.stdev(times) if iterations > 1 else 0,
        "PeakMem": peak_memory_bytes / (1024 * 1024),  # Convert to MB
        "CPU": cpu_usage
    }


def print_markdown_table(results):
    print(f"| {'Method':<27} | {'Mean':>10} | {'StdDev':>10} | {'Peak Memory':>12} | {'CPU %':>8} |")
    print(f"|{'-' * 29}|{'-' * 12}|{'-' * 12}|{'-' * 14}|{'-' * 10}|")

    for r in results:
        name = r["Method"]
        mean = f"{r['Mean']:.2f} ms"
        stdev = f"{r['StdDev']:.2f} ms"
        mem = f"{r['PeakMem']:.3f} MB"
        cpu = f"{r['CPU']:.1f} %"

        print(f"| {name:<27} | {mean:>10} | {stdev:>10} | {mem:>12} | {cpu:>8} |")


if __name__ == "__main__":
    print("Running benchmarks, please wait...\n")

    results = []

    # Test your prime generator at different scales
    test_values = [100, 1000, 10000, 100000]

    for n in test_values:
        data = benchmark_function(f"Prime Gen (n={n})", primes.gen_primes, n, iterations=30)
        results.append(data)

    # Print the final Markdown Table
    print_markdown_table(results)