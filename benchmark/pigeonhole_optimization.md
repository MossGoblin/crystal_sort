# pigeon hole optimization

Built on top of the basic crystal sort algorithm.

The inner iteration is replaced by another step.

* [Method](#method)
* [Example](#example)
* [Usage](#usage)

### Method

The process of iterating is called bracketing. Each iteration takes a subset of the array (starting with the full array) and creates a bracket.

The primary pass of the iteration finds the lowest and higherst values of the subset and places them at the first and last indices of the subset (same as outer iteration of crystal sort).

A remainder is defined as the subset minus the first and last element.

A secondary pass is made over the remainder. It returns atuple of the following:

- all the elements, equal to the lowest element of the parent subset.
- all elements not equal to the lowest or highest element in the parent subset.
- all the elements, equal to the highest element of the parent subset.

After the secondary pass the returned values are combined with the lowest and highest elements in the parent subset.

The iteration returns the following tuple:

- lower bracket: The lowest element of the subset and all elements with the same value
- remainder: All elements that differ from the lowest and the highest element
- higher bracket: The highest element of the subset and all elements with the same value

After the iteration the lower bracket and teh higher bracket are added to the brackets from previous iterations.

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
# size of array equal to elements possible size
10000 runs
element values: 1..10000
random values
(base / pigeon hole)
time: 0:00:10.357593 / 0:00:16.832661 (162.52 %)
passes: 25000000 / 31441982 (125.77 %)
comparisons: 50054091 / 45400197 (90.70 %)
swaps*: 6140815 / 3581734 (58.33 %)

# size of array larger than elements possible size
10000 runs: 1..1000
random
time: 0:00:10.728186 / 0:00:02.823458 (26.32 %)
passes: 25000000 / 5050124 (20.20 %)
comparisons: 50071664 / 7534087 (15.05 %)
swaps*: 1490966 / 82949 (5.56 %)

# size of array much larger than elements possible size
100000 runs
element values: 1..10
random values
(base / pigeon hole)
time: 0:17:14.631099 / 0:00:00.463996 (0.04 %)
passes: 2500000000 / 554358 (0.02 %)
comparisons: 4999980816 / 876029 (0.02 %)
swaps*: 167968 / 9 (0.01 %)

(* "swaps" is not a reliable metric, as the secondary pass of the pigeon hole algorithm does not use direct swapping of elements and no equivalent metric is used in it's stead)
```

### Possible development

Implementing both versions of the algorithm as one module with an optional argument for indicating when the input array has not duplicate values.

```python
crystal_sort.sort(array, unique=True)
```

### Name

The optimization is called '**pigeon hole**' as the algorithm takes advantage of the pigeon hole principle - if the range of possible values for the elements is smaller than the size of the array, then duplicate values are guaranteed.