import multiprocessing
import time
import random
import os


# ---------- Chef process (uses Queue to communicate) ----------
def chef_with_queue(order_queue, status_queue):
    """
    Chef reads orders from order_queue and sends status updates via status_queue.
    """
    while True:
        try:
            order = order_queue.get(timeout=3)  # wait for order
        except:
            break  # no more orders
        if order == "STOP":
            print(f"[Chef-{os.getpid()}] Stopping.")
            break

        # simulate cooking
        print(f"[Chef-{os.getpid()}] Cooking {order}...")
        cook_time = random.randint(2, 6)
        time.sleep(cook_time)
        status_queue.put(f"{order} ready by Chef-{os.getpid()} in {cook_time}s")


# ---------- Waiter process (uses Pipe to communicate) ----------
def waiter(pipe_conn):
    """
    Waiter receives ready dishes through a pipe and delivers them.
    """
    while True:
        msg = pipe_conn.recv()
        if msg == "CLOSE":
            print("[Waiter] Closing service.")
            break
        print(f"[Waiter] Delivered: {msg}")


# ---------- Main function ----------
if __name__ == "__main__":
    print("=== Restaurant Simulation ===")

    # Queues for communication
    order_queue = multiprocessing.Queue()
    status_queue = multiprocessing.Queue()

    # Pipe for waiter communication
    parent_conn, child_conn = multiprocessing.Pipe()

    # Spawn chef processes
    chefs = [multiprocessing.Process(target=chef_with_queue, args=(order_queue, status_queue))
             for _ in range(3)]

    # Start chefs
    for chef in chefs:
        chef.start()

    # Spawn waiter process
    waiter_proc = multiprocessing.Process(target=waiter, args=(child_conn,))
    waiter_proc.start()

    # Send orders to chefs
    orders = ["Burger", "Pizza", "Pasta", "Salad", "Fries", "Steak"]
    for o in orders:
        order_queue.put(o)

    # Simulate manager monitoring chefs
    start_time = time.time()
    timeout = 10  # seconds

    while time.time() - start_time < timeout:
        try:
            # receive ready dish updates
            msg = status_queue.get(timeout=1)
            print(f"[Manager] Got update: {msg}")
            parent_conn.send(msg)
        except:
            pass  # no updates yet

    # If some chefs are still cooking, manager may kill one
    print("\n[Manager] Time's up! Checking for slow chefs...")
    for chef in chefs:
        if chef.is_alive():
            print(f"[Manager] Terminating Chef-{chef.pid} (too slow!)")
            chef.terminate()  # 🔥 Kill process
            chef.join()

    # Stop remaining chefs and waiter
    for _ in chefs:
        order_queue.put("STOP")

    parent_conn.send("CLOSE")
    waiter_proc.join()

    print("\n=== Simulation Ended ===")
