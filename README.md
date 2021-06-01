# crystal_sort

Sorting algorithm, using swapping.

### Features:

* the algorithm always makes a fixed number of passes over the array, equal to half the length of the array

* works with both integers and floating point numbers

### Time Complexity:

As the number of iteration is fixed, the running time is the same for all cases (worst case, slightly randomized, ordered, reversed).

Comparison was made with *insertion sort*:

- *crystal sort* has lower iteration count - half the length; iteration sort has length - 1 iterations.

- the number of value comparisons and element rearrangements of *insertion sort* is almost exactly 90% of the respective numbers for *crystal sort*.

### Method

In each iteration smaller and smaller subset of the array is processed.

An offset is defined, equal to the index of the iteration (0, 1, 2...).

Before each iteration, the offset is applied. The subset that the iteration will be performed on, is produced by shrinking the previous subset at each end by a number of elements equal to the current offset.

- In the first iteration the offset is 0, so the iteration is performed over the whole array.

- Each element of the array in turn is selected as 'seed'. The seed is compared to the last element of the subset and swapped with it, if the seed is strictly higher. If not - it is compared to the first element of the subset and swapped with it, if the seed is strictly lower. When the seed is the first element of the subset, the second comparison does not yield result, as the algorithm compares an element with itself.

- *At the end of thе first iteration the first element of the set is guaranteed to be the smallest, and the last element is guaranteed to be the largest.*
* After the iteration, the offset is increased and the resulting subset is iterated over.

* The offset increases until it reaches half the length of the full set. At this point the full array can be seen as a series of element pairs, bracketing each other. The outermost pair contains the smallest and the largest elements. The second pair (indices 1 and -2) contains the second smallest and second largest elements and so on.

The sorting algorithm is called **crystal sort**, because the way the set gets ordered from the ends towards the middle reminiscent of crystalization. This is also the reason the element that is being currently compared is called **seed**.