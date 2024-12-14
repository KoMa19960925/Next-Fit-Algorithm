# Function to allocate memory to processes using the Next Fit algorithm.
def next_fit(block_size, process_size):
    """
    block_size: List containing sizes of memory blocks.
    process_size: List containing sizes of processes to allocate.
    """
    # Total number of memory blocks and processes to allocate
    num_blocks = len(block_size) 
    num_processes = len(process_size)  

    # Tracks the block allocated to each process
    allocation = [-1] * num_processes

    # Start allocation from the first block
    j = 0

    # Iterate through each process
    for i in range(num_processes):
        # Check all blocks starting from the current position 
        count = 0  # To avoid infinite loops
        while count < num_blocks:
            if block_size[j] >= process_size[i]:
                # Allocate the block to the process
                allocation[i] = j
                # Reduce the size of the block after allocation
                block_size[j] -= process_size[i]
                break

            # Move to the next block (circular manner)
            j = (j + 1) % num_blocks
            count += 1

    # Display the allocation results
    print("Process No.\tProcess Size\tBlock No.")
    for i in range(num_processes):
        print(f"{i + 1}\t\t{process_size[i]}\t\t", end="")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            # Indicate that the process was not allocated
            print("Not Allocated")

# Driver Code
if __name__ == "__main__":
    # Memory block sizes and process sizes as per the example
    block_size = [12, 18, 22, 15]
    process_size = [10, 20, 15, 30]

    # Call the Next Fit memory allocation function
    next_fit(block_size, process_size)
