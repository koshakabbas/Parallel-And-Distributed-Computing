from mpi4py import MPI
def main():
    comm = MPI.COMM_WORLD
    rank = comm.rank
    size = comm.size

    print(f"Process {rank} of {size} is running...")

    # ---------- Original Logic ----------
    if rank == 0:
        data = 10000000
        destination_process = 4
        comm.send(data, dest=destination_process)
        print(f"[Rank {rank}] Sent data {data} to process {destination_process}")

    elif rank == 1:
        data = "hello"
        destination_process = 8
        comm.send(data, dest=destination_process)
        print(f"[Rank {rank}] Sent data '{data}' to process {destination_process}")

    elif rank == 4:
        data = comm.recv(source=0)
        print(f"[Rank {rank}] Received data = {data} from process 0")

    elif rank == 8:
        data1 = comm.recv(source=1)
        print(f"[Rank {rank}] Received data1 = '{data1}' from process 1")

    else:
        print(f"[Rank {rank}] No communication assigned for this process.")

    # ---------- Barrier sync ----------
    comm.Barrier()
    if rank == 0:
        print("\n=== MPI Communication Completed Successfully ===")


if __name__ == "__main__":
    main()
