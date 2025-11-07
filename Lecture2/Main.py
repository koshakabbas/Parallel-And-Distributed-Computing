import threading
import time
import random

# -------------------------------
# Example: Car Wash Simulation
# -------------------------------
# - Only 2 washing machines available (Semaphore)
# - Wait until all cars are washed (Barrier)
# - Notify manager when all cars done (Condition)
# - Safe logging using RLock
# -------------------------------

wash_slots = threading.Semaphore(2)        # Only 2 cars can be washed at once
num_cars = 4                               # Total cars to wash
wash_barrier = threading.Barrier(num_cars) # Wait until all cars are washed
manager_condition = threading.Condition()  # Manager waits until all are done
log_lock = threading.RLock()               # Safe logging

washed_cars = []


def log(msg):
    """Thread-safe print using RLock"""
    with log_lock:
        print(msg)


def car(car_id):
    """Each car tries to use a washing machine."""
    log(f"Car {car_id} arrived at car wash.")
    with wash_slots:
        log(f"Car {car_id} is being washed.")
        time.sleep(random.uniform(1, 3))
        log(f"Car {car_id} finished washing.")

    # Wait for other cars to finish
    wash_barrier.wait()
    log(f"Car {car_id} is ready to leave.")

    # Notify manager
    with manager_condition:
        washed_cars.append(car_id)
        manager_condition.notify()


def manager():
    """Manager waits until all cars are washed."""
    with manager_condition:
        while len(washed_cars) < num_cars:
            manager_condition.wait()
        log("Manager: All cars have been washed. Closing car wash.")


def main():
    log("Car wash opens.")
    t_manager = threading.Thread(target=manager)
    t_manager.start()

    cars = []
    for i in range(1, num_cars + 1):
        t = threading.Thread(target=car, args=(i,))
        cars.append(t)
        t.start()

    for t in cars:
        t.join()

    t_manager.join()
    log("Car wash closed.")


if __name__ == "__main__":
    main()
