# crystal sort

**Sorting algorithm, using iterative swapping.**

* [Usage](#usage)
* [Time complexity](#complexity)
* [Naming](#naming)
* [Method](#method)
* [Pros/Cons](#proscons)
* [Comparison](#comparison)

---

## Usage

```python
from crystal_sort import crystal_sort

array1 = [5, 4, 1, 3, 8, 5, 6]
array2 = [2.3, -3.5, 77.14, 77.1, -1, 0]
array3 = [0, 0, 1, 2, 6, 6, 9, 8, 8, 7, 7, 7]

print(crystal_sort.sort(array1))

print(crystal_sort.sort(array2))

# the explicit use of True flag in here is only as example;
print(crystal_sort.sort(array3, True))
```

```
Output:
[1, 3, 4, 5, 5, 6, 8]
[-3.5, -1, 0, 2.3, 77.1, 77.14]
[0, 0, 1, 2, 6, 6, 7, 7, 7, 8, 8, 9]
```

---

## Complexity:

The number of iterations depends on the size of the array, which makes the Big-O value of *crystal sort*  **O(n^2)**

---

## Naming

The sorting algorithm is called **crystal sort**, because the way the set gets ordered from the ends towards the middle reminiscent of crystallization. This is also the reason the element that is being currently compared is called **seed**.

The secondary operation is called '**pigeon hole**' optimization as the algorithm takes advantage of the pigeon hole principle - if the range of possible values for the elements is smaller than the size of the array, then duplicate values are guaranteed. (*see Secondary operation*)

---

## Method

The algorithm uses one primary iteration and an optional secondary one.

### Primary iteration

**Short descrption:**

Each iteration is composed of two operations:

* In the current subset the smallest and largest values are found in a single pass; those values and the remainder are passed as input to the secondary operation

* From the remainder all values that equal the smallest element from the first operation and the ones that equal the largest element are extracted; those two groups of values and the remaining values are returned
  
  * The groups of equal values from the second operation are combined with the smallest and largest values from the first operation. The remainder of the second operation is passes as input to another pass of the primary operation.

**Detailed description:**

The inner iteration is of decreasing length.

In each primary iteration increasingly smaller subsets of the array are processed. Each primary iteration results in two elements placed in their proper place.

* A subset of the array is being iterated upon. Each element of the subset is compared with the first and last element and swapped with one of them.

* At the end of the primary iteration the smallest element is always at the beginning of the subset, the largest is always at the end of the subset.
  
  *At the end of the first iteration the first element of the set is guaranteed to be the smallest, and the last element is guaranteed to be the largest.*

* The first and the last element of the previous subset are *crystalized* - the first element is added to the end of a *lower_ordered_set* array, and the last element is added to an *upper_ordered_set*. Then they are removed from the subset, forming a new subset.

* The sort() method has a *duplicates* flag that denotes whether the secondary operation is to be applied.

* The flag is set to rue by default, taking under consideration the fact that the algorithm performs well only in cases when there are many duplicate values in the input array. See *Secondary iteration consideration* below.

* **If** the flag is False, the new subset is sent for another primary iteration.

* **If** the flag is True, the subset is sent for a secondary operation.

* ### Secondary operation (optional)

* This operation is called *pigeonhole optimization*

* The secondary operation takes 3 arguments: the smallest and largest values, determined by the primary iteration and the new subset.

* This subset is split into three parts - an array of all elements (*lower_addition*), equal to the passed low value, an array of all elements, equal to the passed high value (*upper_addition*) and an array, containing the remaining values (*remainder*).

* The *lower_addition* array is added to the end of the *lower_ordered_set* and the *upper_addition* is added to the end of the *upper_ordered_set*.

* The remainder is sent as a new subset for a primary iteration.

* After each primary (and optional secondary) iteration the lower and upper ordered sets grow, until the remaining subset contains either 0 elements, 1 element or only duplicate elements.

### Secondary iteration consideration

If the maximum range of values in the array is smaller than the number of values, then it is certain that the array contains duplicate values. The secondary iteration extracts all values, equal to the smallest and largest values found by each primary iteration. The more duplicate values the array contains, the more work is done by the secondary iteration. This means fewer primary iterations are performed and in in cases when the possible value range is much smaller than the size of the array, the algorithm performs significantly better.

### Use of secondary operation

The secondary operation is disabled by default. It should be used when duplicate values are known to be prominent or expected to be prominent in the array.

In case of random or arbitrary values, a good rule of thumb is to enable set the pigeonhole flag to True is the range of values for the array elements is one or more orders of magnitude smaller than the size of the array.

---

## Pros/Cons

***Pros***: easy to understand and (in my opinion) elegantly simple

***Cons***: multiple iterations, even in case of ordered starting array; not especially fast for the majority of business cases; works well only for collections with multiple duplicate values and even in such cases is outperformed by *insertion sort*.

---

## Comparison

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

### Comparison with other algorithms

I made a comparison with 5 other sorting algorithms.
The code was lifted directly from
https://stackabuse.com/sorting-algorithms-in-python

The results show two things:

- *crystal sort* with *duplicates* flag False performs poorly in all of the cases, just a bit better than selection sort.
- *crystal sort* with *duplicates* flag True has variable performance, strongly depending on the presence of duplicate numbers in the input array. In the best case tested here (10000 numbers, values ranging from 0 to 10) it ranks second after insertion sort.

Possible problems with the comparison - I have not made any effort to check if the code for the other sorting algorithms can be optimized and to what extent. None of the values are particularly close and the ranking would unlikely change if the code is refactored, but still, I assume the code is optimal.

Results of the comparison:
(**crystal_sort** denotes crystal sort with duplicates flag set to False, ***crystal_sort_pgh*** has the flag set to True)

**500 runs**

**array size 10000**

**values magnitude 10**

| algorithm              | time (microseconds) |
| ---------------------- | ------------------- |
| insertion_sort         | 1420.998            |
| ***crystal_sort_pgh*** | 10211.188           |
| quick_sort             | 17721.764           |
| merge_sort             | 27517.068           |
| heap_sort              | 41853.304           |
| **crystal_sort**       | 375186.43           |
| selection_sort         | 382922.282          |

**500 runs**

**array size 10000**

**values magnitude 100**

| algorithm              | time (microseconds) |
| ---------------------- | ------------------- |
| insertion_sort         | 1312.916            |
| quick_sort             | 14075.374           |
| merge_sort             | 23736.192           |
| heap_sort              | 41056.432           |
| ***crystal_sort_pgh*** | 51481.86            |
| **crystal_sort**       | 361190.068          |
| selection_sort         | 416556.972          |

**500 runs**

**array size 10000**

**values magnitude 1000**

| algorithm              | time (microseconds) |
| ---------------------- | ------------------- |
| insertion_sort         | 1294.872            |
| quick_sort             | 12883.328           |
| merge_sort             | 23462.034           |
| heap_sort              | 44858.044           |
| **crystal_sort**       | 339551.916          |
| selection_sort         | 437169.926          |
| ***crystal_sort_pgh*** | 474806.436          |

**100 runs**

**array size 100**

**equal values**

| algorithm              | time (microseconds) |
| ---------------------- | ------------------- |
| insertion_sort         | 106.19              |
| ***crystal_sort_pgh*** | 460.3               |
| heap_sort              | 559.39              |
| quick_sort             | 1329.84             |
| merge_sort             | 1889.71             |
| **crystal_sort**       | 23203.97            |
| selection_sort         | 23963.37            |