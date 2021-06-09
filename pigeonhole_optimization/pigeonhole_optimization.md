# pigeon hole optimization

Built on top of the basic crystal sort algorithm.

An additional step is added between the inner iteration of crystal sort.

* [Method](#method)
* [Example](#example)
* [Usage](#usage)

### Method

The process of iterating is called bracketing. Each iteration takes a subset of the array (starting with the full array) and creates a bracket.

The primary pass of the iteration finds the lowest and higherst values of the subset and places them at the first and last indices of the subset (same as outer iteration of crystal sort).

The bracket consists of the first element (lowest value), the last element (highest value) and the remainder between them.

A secondary pass is made over the remainder. It returns a tuple of the following:

- all the elements, equal to the lowest element of the parent subset.
- all elements not equal to the lowest or highest element in the parent subset.
- all the elements, equal to the highest element of the parent subset.

After the secondary pass the returned values are combined with the lowest and highest elements in the bracket.

The iteration returns the following tuple:

- lower bracket set: The lowest element of the subset and all elements with the same value
- remainder: All elements that differ from the lowest and the highest element
- higher bracket set: The highest element of the subset and all elements with the same value

After the iteration the lower bracket set and the higher bracket set are added to the bracket sets from previous iterations.

The remainder, if any, goes for another iteration.

### Example

[7, 7, 3, 3, 4, 4, 3, 6]

1st iteration/bracketing

- primary pass:
  
  - input: [7, 7, 3, 3, 4, 4, 3, 6]
  - output: [3, 7, 6, 3, 4, 4, 3, 7]

- secondary pass
  
  - input: 3, [7, 6, 3, 4, 4, 3], 7
  - output: [3, 3], [6, 4, 4], [7]

- combining:
  
  - input:
    - start and end global brackets = [], []
    - 3 and 7 from the input of the secondary pass
    - the output of the secondary pass
  - output: [] + 3 + [3, 3], [6, 4, 4], + 7 + [7] + []
    - [3, 3, 3], [6, 4, 4], [7, 7]
    - the end brackets are combined in reverse order to preserve increating order of elements

2nd iteration:

- primary pass:
  
  - input: [6, 4, 4]
  - output: [4, 4, 6]

- secondary pass
  
  - input: 4, [4], 6
  - output: [4], [ ], [ ]

- combining:
  
  - input:
    - start and end global brackets = [3, 3, 3], [7, 7]
    - 4 and 6 from the input of the secondary pass
    - the output of the secondary pass
  - output: [3, 3, 3] + 4 + [4], [ ], + 6 + [] + [7, 7, 7]
    - [3, 3, 3], [4, 4] + [ ] + [6] + [7, 7]

### Comparison

The difference between teh two version of the algorithm is in the way elements of equal values are handled.

After the lowest and highest values of each subset have been found, the pigeon hole algorithm finds all values, matching one or both of those, moves them to their correct places and excludes them from further iteration.

**Pros/Cons**

For an array with no duplicate values the base version performes better, as each iteration yields a result. In the same time the secondary passes of the pigeon hole version have no valuable return and are wasted. The primary passes essentially perform the base algorithm.

However for an array that has duplicate values, the pigeon hole version outperforms the base one. The size of the difference depends on the mean number of duplicate values - the greater teh duplicates, the more work is done by the secondary pass and the fewer primary passes.

The effect of that would vary between implementations, as the current Python version relies on built-in array manipulation, which in other languages may have different effectiveness measures.

For the current code the effect of the optimization for arrays with high proportion of duplicate values is very pronounced.

In the examples below it can be seen that if the maximum size of the elements is comparable to the size of the array (meaning that few duplicate values are expected), the base version outperforms the pigeon hole version.

If the size of the array is greater than the possible size of the elements, the pigeon hole performs much better.

```
# size of array equal to elements possible size - 10000
10000 runs
element values: 1..10000
random values
(base / pigeon hole)
time: 0:00:13.068543 / 0:00:13.262321 (101.48 %)
passes: 25000000 / 15661947 (62.65 %)
(comparisons: 50003845 / 29529205 (59.05 %))
(swaps: 6115189 / 3530025 (57.73 %))

# size of array larger than elements possible size
100000 runs: 1..10000
random values
(base / pigeon hole
time: 0:21:01.428151 / 0:03:19.442263 (15.81 %)
passes: 2500000000 / 249914185 (10.00 %)
(comparisons: 5000985218 / 495735561 (9.91 %))
(swaps: 150077416 / 8062430 (5.37 %))

# size of array much larger than elements possible size
100000 runs
element values: 1..10
random values
(base / pigeon hole)
time: 0:19:09.614440 / 0:00:00.355971 (0.03 %)
passes: 2500000000 / 278516 (0.01 %)
(comparisons: 4999979699 / 557018 (0.01 %))
(swaps: 167751 / 9 (0.01 %))
```

Swaps and Comparisons are not reliable metrics.
* Comparisons measures the number of 'if' statements, swaps measures direct swaps of two elements in an array.
* The pigeon hole version measures it's primary iterations the same way as the base version does. However the secondary pass does not use ifs nor swaps, so there are no values for those from the secondary passes.
* Passes remains more or less sable as a metric.
* Total time is, of course, fine.

### Possible development

Implementing both versions of the algorithm as one module with an optional argument for indicating when the input array has not duplicate values.

```python
crystal_sort.sort(array, unique=True)
```

### Name

The optimization is called '**pigeon hole**' as the algorithm takes advantage of the pigeon hole principle - if the range of possible values for the elements is smaller than the size of the array, then duplicate values are guaranteed.