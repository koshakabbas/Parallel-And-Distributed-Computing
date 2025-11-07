# main.py
from MyThreadClass import MyThreadClass
import time
from random import randint

def main():
    print("=== Multi-threaded File Downloader Simulation ===\n")
    start_time = time.time()

    # Create threads to simulate file downloads
    threads = []
    for i in range(1, 6):
        duration = randint(2, 8)
        t = MyThreadClass(f"Download_Task_{i}", duration)
        threads.append(t)

    # Start all threads
    for t in threads:
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # End
    print("\nAll downloads complete!")
    print("--- Total Execution Time: %.2f seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()
