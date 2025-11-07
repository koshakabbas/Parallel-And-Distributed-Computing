# Restaurant Simulation — Parallel and Distributed Computing Example

### Course Project Example
This project demonstrates core concepts of **Parallel and Distributed Computing** in Python using the `multiprocessing` module.  
It uses a **real-life analogy** — a **restaurant kitchen** — to show how processes can work in parallel, communicate, and be managed.

---

## Concepts Covered
| Topic | Demonstrated Through | Description |
|--------|---------------------|--------------|
| **Spawning Processes** | `multiprocessing.Process` | Multiple *Chef* processes and a *Waiter* process are created |
| **Communicating with Queues** | `multiprocessing.Queue` | Orders and cooking status updates flow through queues |
| **Communicating with Pipes** | `multiprocessing.Pipe` | Manager and Waiter communicate via a pipe connection |
| **Killing Processes** | `.terminate()` | Manager terminates slow chefs after timeout |

---

## Program Description
In this simulation:
- The **Manager** sends food orders to **Chefs** through a `Queue`.
- Each **Chef** cooks the order (simulated with random time delays) and sends back updates via another `Queue`.
- The **Waiter** listens through a `Pipe` connection and “delivers” ready dishes.
- If a chef takes too long, the **Manager** terminates that process — showing how to **kill** or stop processes in Python.

---

## Project Structure
```
restaurant_simulation/
│
├── restaurant_simulation.py   # Main Python script
└── README.md                  # Project documentation (this file)
```

---

## How to Run the Program

### Requirements
- Python **3.8+**
- Works on **Windows**, **Linux**, or **macOS**

### Steps
1. Clone or download the project folder  
   ```bash
   git clone https://github.com/<your-username>/restaurant_simulation.git
   ```
   *(or simply place `restaurant_simulation.py` and `README.md` together in a folder)*  

2. Open the folder in **VS Code** or any IDE.

3. Run the program:
   ```bash
   python restaurant_simulation.py
   ```

---

## Example Output
```
=== Restaurant Simulation ===
[Chef-11564] Cooking Burger...
[Chef-11565] Cooking Pizza...
[Chef-11566] Cooking Pasta...
[Manager] Got update: Burger ready by Chef-11564 in 2s
[Waiter] Delivered: Burger ready by Chef-11564 in 2s
[Manager] Got update: Pizza ready by Chef-11565 in 3s
[Waiter] Delivered: Pizza ready by Chef-11565 in 3s

[Manager] Time's up! Checking for slow chefs...
[Manager] Terminating Chef-11566 (too slow!)
[Waiter] Closing service.

=== Simulation Ended ===
```

---

## Learning Outcomes
By running and analyzing this program, you’ll understand:
1. How **multiple processes** can execute tasks in **parallel**.
2. How **inter-process communication (IPC)** works using **Queues** and **Pipes**.
3. How to **monitor** and **terminate** processes programmatically.
4. How **parallelism** applies in real-world workflows such as **task distribution** in a kitchen.