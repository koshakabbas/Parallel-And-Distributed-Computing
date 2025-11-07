import multiprocessing
import communicating_with_pipe as pipe_module
def main():
    print("=== PIPE COMMUNICATION DEMO STARTED ===\n")

    # Create first pipe (send numbers 0-9)
    pipe_1 = multiprocessing.Pipe(True)
    process_pipe_1 = multiprocessing.Process(
        target=pipe_module.create_items, args=(pipe_1,)
    )
    process_pipe_1.start()

    # Create second pipe (receive and square numbers)
    pipe_2 = multiprocessing.Pipe(True)
    process_pipe_2 = multiprocessing.Process(
        target=pipe_module.multiply_items, args=(pipe_1, pipe_2,)
    )
    process_pipe_2.start()

    # Close unnecessary pipe ends in the main process
    pipe_1[0].close()
    pipe_2[0].close()

    try:
        while True:
            result = pipe_2[1].recv()
            print(f"Received squared value: {result}")
    except EOFError:
        print("\n=== All data received. Process finished. ===")

    # Ensure processes are joined
    process_pipe_1.join()
    process_pipe_2.join()


if __name__ == "__main__":
    main()
