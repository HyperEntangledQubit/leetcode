#!/usr/bin/env python3

from twosum import two_sum

def test_target_sum_next_to_each_other():
    dummy_array = [2, 7, 11, 15]
    dummy_target = 9

    have = two_sum(dummy_array, dummy_target)
    want = [0, 1]

    if have != want:
        assert False, "two_sum solution did NOT return the correct pair"

def test_target_sum_with_negative_number():
    dummy_array = [-3, 4, 3, 90]
    dummy_target = 0

    have = two_sum(dummy_array, dummy_target)
    want = [0, 2]

    if have != want:
        assert False, "two_sum solution did NOT return the correct pair"

def test_target_sum_with_dupe_number():
    dummy_array = [3, 2, 3]
    dummy_target = 6

    have = two_sum(dummy_array, dummy_target)
    want = [0, 2]

    if have != want:
        assert False, "two_sum solution did NOT return the correct pair"
