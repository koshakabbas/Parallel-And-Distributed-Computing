# Multi-threaded and Multi-processed Python Program

## Overview
This project demonstrates how to use **threads** and **processes** in Python to perform two tasks concurrently:

1. Check if a number is **positive**, **negative**, or **zero**.  
2. Calculate the **sum** of all numbers in a list.

The program runs both tasks using:
- **Threading** – lightweight concurrency within a single process  
- **Multiprocessing** – true parallelism using separate processes  

---

## Concepts Used

### Threading
Threading allows multiple tasks to run **concurrently** within the same process.  
Threads share the same memory space, making them efficient for **I/O-bound** tasks.

**Example:**
```python
t1 = threading.Thread(target=check_number, args=(1,))
t2 = threading.Thread(target=calculate_sum, args=(numbers,))
t1.start()
t2.start()
```

---

### Multiprocessing
Multiprocessing creates **independent processes** that run in **parallel**.  
Each process has its own memory space, making it ideal for **CPU-bound** operations.

**Example:**
```python
p1 = multiprocessing.Process(target=check_number, args=(-4.5,))
p2 = multiprocessing.Process(target=calculate_sum, args=(numbers,))
p1.start()
p2.start()
```

---

## Functions

### `check_number(num)`
Determines whether a number is **positive**, **negative**, or **zero**.

### `calculate_sum(numbers)`
Calculates and prints the **sum** of all numbers in a list.

---

## How to Run

### Step 1: Clone the repository
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### Step 2: Run the Python script
```bash
python main.py
```

### Step 3: View the output
You will see results from both **threading** and **multiprocessing** executions.

---

## Example Output
```
Starting Program Execution...

--- Running with Threads ---
1 is a Positive number
The sum of the list is: 83

--- Running with Processes ---
-4.5 is a Negative number
The sum of the list is: 83

Program Completed.
```

---