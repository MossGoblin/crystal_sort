from copy import deepcopy
from typing import List

__doc__ = """
Sorting algorithm for arrays of numeric values

Functions:
    sort(int[], bool) -> int[]
"""


def sort(incoming_bucket, duplicates=True):
    '''
    Sorts an array of numbers

            Parameters:
                    incoming_bucket (int[]): An array of integers
                    dupplicates (bool): Flag for taking duplicate values into account
                        default: True

            Returns:
                    result_array (int[]): Sorted array of integers
    '''
    def __create_bracket(subset, initial_bracket, lower_value, upper_value):
        search_lower = True
        search_upper = True
        for index in range(0, len(subset)):
            seed = subset[index]
            if search_upper and seed > subset[-1]:
                subset[index], subset[-1] = subset[-1], subset[index]
                if not initial_bracket and seed == upper_value:
                    search_upper = False
                continue
            elif search_lower and seed < subset[0]:
                subset[index], subset[0] = subset[0], subset[index]
                if not initial_bracket and seed == lower_value:
                    search_lower = False
                continue

        return subset[0], subset[-1], subset[1:-1]

    def __combine_lower(lower_end, lower_addition):
        if isinstance(lower_addition, List):
            lower_end = lower_end + lower_addition
        else:
            lower_end = lower_end + [lower_addition]

        return lower_end

    def __combine_higher(upper_end, upper_addition):
        if isinstance(upper_addition, List):
            upper_end = upper_addition + upper_end
        else:
            upper_end = [upper_addition] + upper_end

        return upper_end

    def __extract_duplicates(subset, lower_value, upper_value):
        lower_value_count = 0
        upper_value_count = 0
        remainder = []
        for seed in subset:
            if seed == lower_value:
                lower_value_count += 1
            elif seed == upper_value:
                upper_value_count += 1
            else:
                remainder.append(seed)

        return [lower_value]*lower_value_count, [upper_value]*upper_value_count, remainder

    remainder = deepcopy(incoming_bucket)
    lower_ordered_set = []
    upper_ordered_set = []
    upper_value = 0
    lower_value = 0

    initial_bracket = True
    while len(remainder) > 1:
        lower_value, upper_value, remainder = __create_bracket(
            remainder, initial_bracket, lower_value, upper_value)
        initial_bracket = False
        lower_ordered_set = __combine_lower(lower_ordered_set, lower_value)
        upper_ordered_set = __combine_higher(upper_ordered_set, upper_value)
        if not duplicates:
            continue
        if lower_value != upper_value:
            lower_addition, upper_addition, remainder = __extract_duplicates(
                remainder, lower_value, upper_value)
            if len(lower_addition) > 0:
                lower_ordered_set = __combine_lower(
                    lower_ordered_set, lower_addition)
            if len(upper_addition) > 0:
                upper_ordered_set = __combine_higher(
                    upper_ordered_set, upper_addition)
        else:
            break

    result_array = lower_ordered_set + remainder + upper_ordered_set

    return result_array
