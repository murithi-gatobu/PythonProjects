# Define a higher-order function named 'count'
def count(predicate, lst):
    result = 0  # Step 1: Initialize counter

    # Step 2: Traverse the list
    for x in lst:
        # Step 3: Apply the test
        if predicate(x):
            result += 1  # Step 4: If test is True, increment count

    return result  # Step 5: Return final count

# Count how many numbers are greater than 2
print(count(lambda x: x > 2, [1, 2, 3, 4, 5]))  # Output: 3

# Count how many numbers are even
print(count(lambda x: x % 2 == 0, [1, 3, 4, 6]))  # Output: 2
