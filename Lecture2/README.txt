Car Wash Simulation (Python Threading)

This project is part of **Chapter 2** from the course **Parallel and Distributed Computing (23SP-047-CS)**.  
It demonstrates the use of Python’s threading and synchronization mechanisms through a car wash simulation.

---

Folder Location

Repository: [Parallel-distributed-computing-23sp-047-cs](https://github.com/safwansamad5/Parallel-distributed-computing-23sp-047-cs)  
Folder: `chapter 2`  
File: `main.py`

---

Overview

This simulation models a car wash system where:
- Only 2 washing machines are available at a time.
- Multiple cars arrive and wait for their turn.
- A manager oversees and closes the car wash once all cars are done.

It uses synchronization tools from Python’s `threading` module, including:
- Semaphore  
- Barrier  
- Condition  
- Reentrant Lock (RLock)

---

Concepts Demonstrated

| Synchronization Primitive | Purpose |
|----------------------------|----------|
| Semaphore | Limits access to washing machines (2 cars at a time). |
| Barrier | Ensures all cars finish washing before leaving. |
| Condition | Notifies the manager once all cars are done. |
| RLock | Enables safe, thread-safe logging to the console. |

---

How It Works

1. Cars arrive at the car wash.
2. Each car waits for a free washing slot (controlled by a semaphore).
3. Once done, the car waits at a barrier until all cars have finished.
4. Each car notifies the manager when done.
5. The manager waits until all cars are finished before closing the wash.

---

Example Output

```

Car wash opens.
Car 1 arrived at car wash.
Car 2 arrived at car wash.
Car 1 is being washed.
Car 2 is being washed.
Car 3 arrived at car wash.
Car 4 arrived at car wash.
Car 1 finished washing.
Car 3 is being washed.
Car 2 finished washing.
Car 4 is being washed.
Car 3 finished washing.
Car 4 finished washing.
Car 1 is ready to leave.
Car 2 is ready to leave.
Car 3 is ready to leave.
Car 4 is ready to leave.
Manager: All cars have been washed. Closing car wash.
Car wash closed.

````

---

Run the Simulation

1. Clone the repository:
   ```bash
   git clone https://github.com/safwansamad5/Parallel-distributed-computing-23sp-047-cs.git
````

2. Navigate to the folder:

   ```bash
   cd "Parallel-distributed-computing-23sp-047-cs/chapter 2"
   ```
3. Run the simulation:

   ```bash
   python main.py
   ```

---

License

This project is licensed under the MIT License.

---

Acknowledgment

This project demonstrates practical use of Python’s threading module — ideal for understanding synchronization, concurrency control, and coordination in parallel systems.

