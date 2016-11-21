__author__ = 'ankur'

import sys


def merge_sort(input_array):
    if len(input_array) == 1:
        return input_array
    else:
        middle = int(len(input_array) / 2)
        left_sort_input = merge_sort(input_array[:middle])
        right_sort_input = merge_sort(input_array[middle:])
        merged_array = merge(left_sort_input, right_sort_input)
        return merged_array


def merge(left_sort_input, right_sort_input):
    merged_array = []
    left_index, right_index = 0, 0
    total_length = len(left_sort_input) + len(right_sort_input)
    for i in range(total_length):
        if (((left_index < len(left_sort_input) and (right_index < len(right_sort_input))) and (
            left_sort_input[left_index] <= right_sort_input[right_index])) or (right_index >= len(right_sort_input))):
            merged_array.append(left_sort_input[left_index])
            left_index += 1
        elif (((left_index < len(left_sort_input) and (right_index < len(right_sort_input))) and (
            left_sort_input[left_index] > right_sort_input[right_index])) or (left_index >= len(left_sort_input))):
            merged_array.append(right_sort_input[right_index])
            right_index += 1
    return merged_array


if __name__ == "__main__":
    input_array = sys.argv[1:]
    sorted_array = merge_sort(input_array)
    print("Sorted Array : " + str(sorted_array))




