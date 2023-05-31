
def twoSum(array, target):
    """ Initial attempt at solving two sum problem.

    Iterating through the array twice yields a O(n^2) solution. We can do
    better.

    Args:
        array (list): List of ints to search for sum.
        target (int): Int value we are searching for.

    Examples:
        >>> array = [0, 6, 2, 7, 12]
        >>> target = 13
        >>> twoSum(array, target)
        [1, 3]

    Returns:
        list of indexes containing the two numbers that sum to our target.
    """
    result = []
    for i in range(len(array)):
        # Stopping at two results here. Omit condition for 3-sum or N-sum.
        if len(result) == 2:
            break
        for j in range(len(array)):
            if i != j: # Omit dupes
                if array[i] + array[j] == target:
                    result.append(i)
                    result.append(j)
                    break
    return result
