import json
import threading
import time
import asyncio
from collections import Counter, defaultdict, namedtuple, deque
import matplotlib.pyplot as plt

# Decorator to measure execution time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of '{func.__name__}': {end_time - start_time:.6f} seconds")
        return result
    return wrapper

# Exception handling for data input
def get_data_from_user():
    try:
        n = int(input("Enter number of data points: "))
        data = []
        for i in range(n):
            value = float(input(f"Enter value {i+1}: "))
            data.append(value)
        return data
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return []

# Asynchronous data fetch simulation
async def async_data_fetch(delay, name):
    print(f"Fetching {name}...")
    await asyncio.sleep(delay)
    print(f"Fetched {name}.")
    return [delay * i for i in range(1, 6)]

# Data processing using collections
@timing_decorator
def process_data(data):
    counter = Counter(data)
    grouped = defaultdict(list)
    for value in data:
        grouped[value % 2].append(value)  # Group by even/odd
    return counter, grouped

# Visualization
def visualize_data(data):
    plt.figure(figsize=(8, 4))
    plt.hist(data, bins=10, color='skyblue', edgecolor='black')
    plt.title("Data Distribution")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()

# Export data to JSON
def export_to_json(data, filename="analysis_output.json"):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Data exported to {filename}")
    except Exception as e:
        print(f"Error exporting data: {e}")

# Multithreading example: Calculate squares and cubes
def calculate_squares(data):
    print("Squares:", [x**2 for x in data])

def calculate_cubes(data):
    print("Cubes:", [x**3 for x in data])

def run_multithreaded_tasks(data):
    t1 = threading.Thread(target=calculate_squares, args=(data,))
    t2 = threading.Thread(target=calculate_cubes, args=(data,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__main__":
    # Data input
    user_data = get_data_from_user()
    if not user_data:
        user_data = [1, 2, 3, 4, 5]  # fallback data

    # Async fetch and merge
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    fetched_data = loop.run_until_complete(asyncio.gather(
        async_data_fetch(1, "AsyncData1"),
        async_data_fetch(2, "AsyncData2")
    ))
    merged_data = user_data + fetched_data[0] + fetched_data[1]

    # Data processing
    counter, grouped = process_data(merged_data)
    print("Counter:", counter)
    print("Grouped (Even/Odd):", dict(grouped))

    # Visualization
    visualize_data(merged_data)

    # Export
    export_to_json({
        "original_data": user_data,
        "merged_data": merged_data,
        "counter": dict(counter),
        "grouped": {str(k): v for k, v in grouped.items()}
    })

    # Multithreading
    run_multithreaded_tasks(merged_data)

    # namedtuple and deque usage
    Record = namedtuple('Record', ['id', 'value'])
    records = deque([Record(i, v) for i, v in enumerate(merged_data)])
    print("First record:", records[0])
    records.appendleft(Record(-1, 0))
    print("Deque after appendleft:", records)