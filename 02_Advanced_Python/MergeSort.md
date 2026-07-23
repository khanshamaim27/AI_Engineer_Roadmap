1. Merge Sort Algorithm
Definition:

Merge Sort is a sorting algorithm that uses the Divide-and-Conquer technique. It divides a list into smaller parts, sorts them, and then merges them back together.

Steps:
Divide the list into two halves.
Recursively divide until each part has one element.
Merge smaller lists in sorted order.
Return the final sorted list.
Example:
Original:
[8, 3, 5, 1]

Divide:
[8,3]   [5,1]

Divide:
[8] [3] [5] [1]

Merge:
[3,8] [1,5]

Final:
[1,3,5,8]
Key Points:
Uses recursion.
Uses Divide-and-Conquer.
Stable sorting algorithm.
Does not modify original list unless implemented in-place.
Complexity:
Type	Complexity
Best Case	O(n log n)
Average Case	O(n log n)
Worst Case	O(n log n)
Space	O(n)

# Merge Sort Algorithm

## Visualization

![Merge Sort Visualization](images/merge_sort.gif)


## Algorithm

1. Divide the list into two halves.
2. Sort both halves recursively.
3. Merge the sorted halves.


## Complexity

Time Complexity: O(n log n)

Space Complexity: O(n)