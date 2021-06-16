# crystal sort

**Sorting algorithm, using iterative swapping.**

* [Features](#features)
* [Naming](#naming)
* [Pros/Cons](#proscons)
* [Time complexity](#complexity)
* [Method](#method)
* [Usage](#usage)

### Features:

* the maximum number of passes that the algorithm makes equals half the length of the array

* works with both integers and floating point numbers

* there is an optional second operation, which can speed up the sort for array with certain properties

### Naming

The sorting algorithm is called **crystal sort**, because the way the set gets ordered from the ends towards the middle is reminiscent of crystalization. 

The secondary operation is called '**pigeon hole**' optimization as the algorithm takes advantage of the pigeon hole principle - if the range of possible values for the elements is smaller than the size of the array, then duplicate values are guaranteed. (*see Secondary operation*)

### Pros/Cons

***Pros***: easy to understand and (in my opinion) elegantly simple

***Cons***: multiple iterations, even in case of ordered starting array; not especially fast

### Time complexity

Each element is iterated more than once. The number of iterations depends on the size of the array, which makes the Big-O value of *crystal sort*  **O(n^2)**

### Method

The algorithm uses one primary iteration and an optional secondary operation.

#### Primary iteration

The primary iteration is of decreasing length.

In each primary iteration increasingly smaller subsets of the array are processed. Each primary iteration results in two elements placed in their proper place.

* A subset of the array is being iterated upon. In the first pass the subset is the whoe starting array. Each element of the subset is compared with the first and last element and swapped with one of them.

* At the end of the primary iteration the smallest element is always at the begining of the subset, the largest is always at the end of the subset.
  
  *At the end of thе first iteration the first element of the set is guaranteed to be the smallest, and the last element is guaranteed to be the largest.*

* The first and the last element of the previous subset are *crystalized* - the first element is added to the end of a *lower_ordered_set* array, and the last element is added to an *upper_ordered_set*. Then they are removed from the subset, forming a new subset.

* The sort() method has a *duplicates* flag that denotes whether the secondary operation is to be applied.

* **If** the flag is False, the new subset is sent for another primary iteration.

* **If** the flag is True, the subset is sent for a secondary operation.

* #### Secondary oprtation (optional)

* This operation is called *pigeonhole optimization*

* The secondary operation takes 3 arguments: the smallest and largest values, determined by the primary iteration and the new subset.

* The subset is split into three parts - an array of all elements, equal to the passed low value (*lower_addition*), an array of all elements, equal to the passed high value (*upper_addition*) and an array, containing the remaining values (*remainder*).

* The *lower_addition* anmd *upper_addition* are crystalized - the *lower_addition* array is added to the end of the *lower_ordered_set* and the *upper_addition* is added to the end of the *upper_ordered_set*.

* The remainder is sent as a new subset for a primary iteration.

* After each primary (and optional secondary) iteration the lower and upper ordered sets grow, until the remaining subset contains either 0 elements, 1 element or only duplicate elements.

### Secondary iteration consideration

If the maximum range of values in the array is smaller than the size of the array, then it is certain that the array contains duplicate values. The secondary iteration extracts all values, equal to the smallest and largest values found by each primary iteration. The more duplicate values the array contains, the more work is done by the secondary operation. This means less primary iterations are performed and in cases when the possible value range is much smaller than the size of the array, the algorithm performes significantly better.

### Use of secondary operation

The econdary operation is disabled by default. It should be used when duplicate values are known to be prominent or expected to be prominent in the array.

In case of random or arbitraty values, a good rule of thumb is to set the *duplicates* flag to True if the range of values for the array elements is one or more orders of magnitude smaller than the size of the array.

### Comparison between modes

Four examples of sorting of random a array with different value magnitudes, comparing the performance of the algorithm with default flag (False) and True.

```python
size:            10000
value mag:       10000
(values: 0..10000)
without / with pigeonhole optimization 
time: 0:00:02.776571 / 0:00:03.249534 (117.03 %)

size:            10000
value mag:        1000
(values: 0..1000)
without / with pigeonhole optimization 
time: 0:00:02.390282 / 0:00:00.487199 (20.38 %)

size:            10000
value mag:         100
(values: 0..100)
without / with pigeonhole optimization 
time: 0:00:02.251711 / 0:00:00.054999 (2.44 %)

size:            10000
value mag:          10
(values: 0..10)
without / with pigeonhole optimization 
time: 0:00:01.896952 / 0:00:00.010999 (0.58 %)
0:03.249534 (117.03 %)
```

### Usage

```python
import crystal_sort

array1 = [5, 4, 1, 3, 8, 5, 6]
array2 = [2.3, -3.5, 77.14, 77.1, -1, 0]
array3 = [0, 0, 1, 2, 6, 6, 9, 8, 8, 7, 7, 7]

print(crystal_sort.sort(array1))

print(crystal_sort.sort(array2))

# the use of True flag in here is only as example;
# for this particular test array the default (False) is recommended
print(crystal_sort.sort(array3, True))
```

```
Output:
[1, 3, 4, 5, 5, 6, 8]
[-3.5, -1, 0, 2.3, 77.1, 77.14]
[0, 0, 1, 2, 6, 6, 7, 7, 7, 8, 8, 9]
```