from copy import deepcopy
from typing import List

def sort(bucket):
    passes = 0
    comparisons = 0
    swaps = 0

    def primary_pass(subset: List):
        passes = 0
        comparisons = 0
        swaps = 0
        for index in range(0, len(subset)):
            passes += 1
            seed = subset[index]
            comparisons += 1
            if seed < subset[0]:
                subset[0], subset[index] = subset[index], subset[0]
                swaps += 1
                continue
            comparisons += 1
            if seed > subset[len(subset)-1]:
                subset[-1], subset[index] = subset[index], subset[-1]
                swaps += 1
                continue
        return subset, passes, comparisons, swaps

    def secondary_pass(lower: int, higher: int, subset: List):
        passes = 0
        comparisons = 0

        start = []
        end = []
        offset_start = 0
        offset_end = 0
        index = 0

        while index < len(subset):
            passes += 1
            seed = subset[index]
            comparisons += 1
            if seed == lower:
                offset_start += 1
            elif seed == higher:
                comparisons += 1
                offset_end += 1
            index += 1

        start = [lower] * offset_start
        remainder = [value for value in subset if (
            value != lower and value != higher)]
        end = [higher] * offset_end
        return start, end, remainder, passes, comparisons

    def process_bracket(subset: List):
        subset, passes_01, comparisons_01, swaps_01 = primary_pass(subset)
        lower = subset[0]
        higher = subset[-1]
        subsubset = subset[1: -1]

        if len(subset) > 1:
            sorted_start, sorted_end, remainder, passes_02, comparisons_02 = secondary_pass(
                lower, higher, subsubset)
        else:
            remainder = subset

        return [lower] + sorted_start, [higher] + sorted_end, remainder, passes_01 + passes_02, comparisons_01 + comparisons_02, swaps_01

    remainder = deepcopy(bucket)
    sorted_start = []
    sorted_end = []

    while len(remainder) > 1:
        sorted_subset_start, sorted_subset_end, remainder, new_passes, new_comparisons, new_swaps = process_bracket(
            remainder)
        sorted_start += sorted_subset_start
        sorted_end = sorted_subset_end + sorted_end

        passes += new_passes
        comparisons += new_comparisons
        swaps += new_swaps

    sorted_bucket = sorted_start + remainder + sorted_end

    return sorted_bucket, passes, comparisons, swaps
