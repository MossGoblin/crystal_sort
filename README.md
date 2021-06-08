# crystal sort

**Sorting algorithm, using iterative swapping.**

* [Features](#features)
* [Pros/Cons](#proscons)
* [Time complexity](#complexity)
* [Method](#method)
* [Example](#example)
* [Usage](#usage)

### Features:

* the algorithm always makes a fixed number of passes over the array, the number being equal to half the length of the array

* works with both integers and floating point numbers

### Pros/Cons

***Pros***: short code; very easy to understand and (in my opinion) elegantly simple

***Cons***: multiple iterations, even in case of ordered starting array; not especially fast

### Time complexity:

The general complexity of *crystal sort* is similar to *insertion sort*, I presume the Big-O value of *crystal sort* is the same - **O(n^2)**

As the number of iteration is fixed, the running time is the same for all cases (worst case, slightly randomized, ordered, reversed).

Comparison was made with *insertion sort*:

- *crystal sort* has lower iteration count - half the length; *insertion sort* has (length - 1) iterations.

- the number of value comparisons and element rearrangements of *insertion sort* is slightly lower - almost exactly 90% of the respective numbers for *crystal sort*.

### Method

The algorithm uses two nested iterations - the outer one iterates a number of times equal to half the length of the array. The inner iteration is of decreasing length.

In each outer iteration increasingly smaller subsets of the array are processed. Each outer iteration results in two elements placed in their proper place.

* Outer iteration - a number of inner iterations equal to half the length of the array.

* An offset is defined, equal to the index of the outer iteration (0, 1, 2...).

* Before each inner iteration, the offset is applied. The subset that the inner iteration will be performed on, is produced by shrinking the previous subset at each end by a number of elements equal to the current offset.
- In the first inner iteration the offset is 0, so the iteration is performed over the whole array.

- Inner iteration - in turn each element of the array is selected as 'seed'. The seed is compared to the last element of the subset and swapped with it, if the seed is strictly higher. If not - it is compared to the first element of the subset and swapped with it, if the seed is strictly lower. When the seed is the first element of the subset, the second comparison does not yield result, as the algorithm compares an element with itself.

- *At the end of thе first iteration the first element of the set is guaranteed to be the smallest, and the last element is guaranteed to be the largest.*
* After the inner iteration, the second inner iteration is performed (outer iteration count + 1); the offset is increased and the resulting subset is iterated over.

* The offset increases until it reaches half the length of the full set. At this point the full array can be seen as a series of element pairs, bracketing each other. The outermost pair contains the smallest and the largest elements. The second pair (indices 1 and -2) contains the second smallest and second largest elements and so on.

The sorting algorithm is called **crystal sort**, because the way the set gets ordered from the ends towards the middle reminiscent of crystalization. This is also the reason the element that is being currently compared is called **seed**.

### Example

array = [5, 4, 1, 3, 8, 5, 6]

Outer iteration 1: offset = 0

**First inner iteration** - over the whole array

* the first seed is at index 0 and has a value of 5
  
  * 5 is not larger than the last element and not smaller than itself, so no swaps are performed.

* the second seed is at index 1 and has a value of 4
  
  * 4 is not larger than 6 (last element); 4 is smaller than the first element, so they are swapped.
  
  * [**5**, **4**, 1, 3, 8, 5, 6]
  
  * [**4**, **5**, 1, 3, 8, 5, 6]

* the third seed is 1; it is smaller than the first element and gets swapped with it:
  
  * [**4**, 5, **1**, 3, 8, 5, 6]
  * [**1**, 5, **4**, 3, 8, 5, 6]

* 4th seed = 3; lower than the last element and larger than the first, so it is not swapped.

* 5th seed = 8; it is higher than the last element, so they are swapped:
  
  * [1, 5, 4, 3, **8**, 5, **6**]
  * [1, 5, 4, 3, **6**, 5, **8**]

* 6th seed = 5; between the first and last element, so no swaps.

* 7th seed = 8; no swaps.

* **The first iteration yields the following array:**
  
  * [**1**, 5, 4, 3, 6, 5, **8**]
    
    The first element is the smallest (1) and the last element is the largest (8)

**Second inner iteration**

Offset = 1;

The subset that will be iterated upon is:

[5, 4, 3, 6, 5]

* 1st seed is 5; no swaps.

* 2nd seed = 4; smaller than the first element; swaps with it.
  
  * [**5**, **4**, 3, 6, 5]
  * [**4**, **5**, 3, 6, 5]

* 3rd seed = 3; smaller than the first element; swaps with it.
  
  * [**4**, 5, **3**, 6, 5]
  * [**3**, 5, **4**, 6, 5]

* 4th seed = 6; larger than the last element; swaps with it.
  
  * [3, 5, 4, **6**, **5**]
  * [3, 5, 4, **5**, **6**]

* 5th seed = 6; no swaps.

At the end of the second iteration the first element of the subset is the smallest in it and the last is the largest.
[**3**, 5, 4, 5, **6**]

The first two elements of the full array are the smallest, increasing with the index; the last two are the largest, also increasing with the index.

* [**1**, **3**, 5, 4, 5, **6**, **8**]

One more inner interaction sorts the remaining [5, 4, 5] in the center to [4, 5, 5]
The final array is ordered:

* [1, 3, 4, 5, 5, 6, 8]

### Usage

```python
import crystal_sort

array1 = [5, 4, 1, 3, 8, 5, 6]
array2 = [2.3, -3.5, 77.14, 77.1, -1, 0]
print(crystal_sort.sort(array1))
print(crystal_sort.sort(array2))
```

```
Output:
[1, 3, 4, 5, 5, 6, 8]
[-3.5, -1, 0, 2.3, 77.1, 77.14]
```