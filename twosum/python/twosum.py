#!/usr/bin/env python3

""" LeetCode TwoSum problem

Given an array and a target value return the two array indexes where their sum
is equal to the target.
"""


def two_sum_dbl_loop(array, target):
    """Initial attempt at solving twosum problem.

    Iterating through the array twice yields a O(n^2) solution.
    We can do better.

    Args:
        array (list): List of ints to search for sum.
        target (int): Int value we are searching for.

    Examples:
        While traversing array should find values 6 and 7 which sum to target.
        Search should cease after finding second value and return list of
        indexes for values 6 and 7.
        >>> array = [0, 6, 2, 7, 12]
        >>> target = 13
        >>> two_sum_dbl_loop(array, target)
        [1, 3]

    Returns:
        list of indexes containing the two numbers that sum to our target.
    """
    result = []
    for i in range(len(array)):  # pylint: disable=consider-using-enumerate
        # Stopping at two results here. Omit condition for 3-sum or N-sum.
        if len(result) == 2:
            break
        for j in range(len(array)):  # pylint: disable=consider-using-enumerate
            if i != j:  # Omit dupes
                if array[i] + array[j] == target:
                    result.append(i)
                    result.append(j)
                    break
    return result


def two_sum_hash(array, target):  # pylint: disable=R1710
    """Instead of iterating through array twice now use a hashmap instead.

    Using a hashmap yields an O(n) solution.

    Args:
        array (list): List of ints to search for sum.
        target (int): Int value we are searching for.

    Examples:
        >>> array = [7, 4, 3, 2, 9]
        >>> target = 16
        >>> two_sum_hash(array, target)
        [0, 4]

    Returns:
        list of indexes containing two numbers that sum to our target.
    """
    hashmap = {}
    for idx, val in enumerate(array):
        if val in hashmap:
            return [hashmap[val], idx]
        hashmap[target - val] = idx
