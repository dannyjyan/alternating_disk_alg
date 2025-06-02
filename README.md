# Alternating Disk Algorithm

This program implements an alternating disk algorithm that sorts a sequence of alternating black and white disks by moving all black disks to the left side using a series of left-to-right and right-to-left passes, with a time complexity of O(n²) and requiring exactly n(n+1)/2 swaps in the worst case.

## How to use it

1. Save the Python file to your computer
2. Create a text file with some code in it
3. Run this command:
   ```
   python alternating_disk.py
   ```

# Pseudocode of Algorithm.
```
def alternating disk_alg(n, S): 
    if n == 1: # base case 
        S[i], S[i+1] = 1, 0
        return S, 1
    swaps = 0
    while (True):
        for i in range(0, 2n-1): # Left to right pass
            if S[i] == 0 and S[i+1] == 1:  # if left is white and right is black
                S[i], S[i+1] = 1, 0
        for i in range(2n-1, 0, -1): # Right to left pass
            if S[i-1] == 0 and S[i] == 1: if left is white and right is black
                S[i-1], S[i+1] = 1, 0
        all_black = True 
        for i in range(n): # Check if the left half is all black pieces
            if S[i] != 1:
                all_black = False
                break
        if all_black: # break out of loop if complete
            break

    return S, swaps
```

Note: Since the algorithm didn't state how to check for completion, I wrote my own which checks the n elements on the left side of the algorithm.

# Big O analysis
The main while loop continues until the first n elements are all black. In the worst case scenario, it need O(n) iterations to move a black disk all the way from the right to the left.

During each iteration, 
Left to right pass is O(2n) operations.
Right to left pass is O(2n) operations.
Checking for all black on the left side is O(n) operations, but can break early.

In total,
O(n) Iterations x
O(2n)+O(2n)+O(n) operations
= O(n) * O(5n)
= O(n^2)

# Results
```
n=1 swaps=1
n=2 swaps=3
n=3 swaps=6
n=4 swaps=10
n=5 swaps=15
```
The number of swaps seems to follow the formula n * (n+1) / 2.
verifying with larger numbers, this seems to be the case.

```
n=10 swaps = 10*11/2 = 55
n=20 swaps = 20*21/2 = 210
n=50 swaps = 50*51/2 = 1275
```
This supports my hypothesis that the formula is O(n^2), as O(n*(n+1)/2) simplifies to O(n^2)

# Possible Improvements
One main improvement is keeping track of how many black pieces there are in row on the left side of the array, and keeping track of how many white pieces. We would have two variables black_index and white_index, which start at 0 and 2n-1, respectively. Instead of interating through the entire array, we'd only go through the portions that are incomplete, reducing the number of elements to check. 

Keeping track of the indexes would have a second benefit of allowing us to have an easier success check that doesn't require iterating through the array. When the black_index reaches n, then the algorithm has finished. This reduces the success check to O(1).