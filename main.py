from itertools import chain, combinations

def generate_partitions(data):
    n = len(data)
    
    # Helper function to get all partitions
    def all_partitions(collection):
        if not collection:
            yield []
            return
        first = collection[0]
        for smaller in all_partitions(collection[1:]):
            for n, subset in enumerate(smaller):
                yield smaller[:n] + [[first] + subset] + smaller[n+1:]
            yield [[first]] + smaller

    # Convert generator output to a list and filter unique partitions
    partitions = list(all_partitions(data))
    
    # Print all partitions
    for partition in partitions:
        print(partition)

    print("\nTotal Partitions:", len(partitions))  # Should match Bell Number B(n)

# Example Usage
generate_partitions([1, 2, 3, 4, 5,6])  # Should produce exactly 5
