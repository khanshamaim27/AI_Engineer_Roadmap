 Selection Sort Algorithm
Definition:
Selection Sort repeatedly finds the smallest element from the unsorted part of the list and places it at the beginning.

Steps:
Start from the first position.
Find the minimum value in the remaining list.
Swap it with the current position.
Move to the next position.
Repeat until sorted.
Example:
Original:
[33, 1, 89, 2]

Pass 1:
Smallest = 1

Swap:
[1, 33, 89, 2]

Pass 2:
Smallest = 2

Swap:
[1, 2, 89, 33]

Final:
[1,2,33,89]
Key Points:
Simple sorting algorithm.
Sorts in-place.
Does not require extra memory.
Avoids unnecessary swaps.
Complexity:
Type	Complexity
Best Case	O(n²)
Average Case	O(n²)
Worst Case	O(n²)
Space	O(1)

# Selection Sort Algorithm

## Visualization

![Selection Sort](images/selection_sort.gif)


## Working

1. Find the smallest element.
2. Swap it with the first unsorted element.
3. Repeat until sorted.


## Complexity

Time: O(n²)

Space: O(1)