# -- Merge sort using recursive function calls
from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:  # -- terminating for array with 1 element
        return arr
    if len(arr) == 2:  # -- terminating for array with 2 elements
        return arr[1:] + arr[:1] if arr[0] > arr[1] else arr

    # -- recursive halving
    temp_arr: List[int] = []
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # merging left and right parts
    left_i = right_i = 0
    while left_i < len(left) and right_i < len(right):
        if left[left_i] < right[right_i]:
            temp_arr.append(left[left_i])
            left_i += 1
        else:
            temp_arr.append(right[right_i])
            right_i += 1
    if left_i < len(left):
        temp_arr.extend(left[left_i:])
    if right_i < len(right):
        temp_arr.extend(right[right_i:])
    return temp_arr


def main():
    num_arr = [23, 2, 24, 12, 2, 3, 4, 5, 6, 6, 389, 23, 32, 90, 24, 7]
    sorted_arr = merge_sort(num_arr)
    print(sorted_arr)
