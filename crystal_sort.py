from copy import deepcopy
import math


def crystal_sort(incoming_bucket):

    def swap(bucket, index_one, index_two):
        temp = bucket[index_one]
        bucket[index_one] = bucket[index_two]
        bucket[index_two] = temp

    bucket = deepcopy(incoming_bucket)
    for offset in range(0, math.floor(len(bucket)/2)):
        subset_start_index = offset
        subset_end_index = - (offset + 1)
        for index in range(subset_start_index, len(bucket) + subset_end_index):
            value = bucket[index]
            if value > bucket[subset_end_index]:
                swap(bucket, index, subset_end_index)
                continue
            else:
                if value < bucket[subset_start_index]:
                    swap(bucket, index, subset_start_index)
                    continue

    return bucket