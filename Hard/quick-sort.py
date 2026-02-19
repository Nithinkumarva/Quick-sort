from typing import List

def quickSort(arr: List[int]) -> List[int]:
    # Your code here
    pass

# Read input
arr = list(map(int, input().split()))
result = quickSort(arr)
print(' '.join(map(str, result)))