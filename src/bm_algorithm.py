# Author: jbuiiii
# Date Created: 17/08/2026

"""
Implementation of Boyer-Moore Algorithm, which improves on naive-pattern matching.
This algorithm is typically seen within grep, and standard find features in web browsers and text editors. 

Avoids unnecessary right-to-left scans using three rules:
- Bad Character Rule
- Good Suffix Rule
- Matching Prefix Rule
"""

from typing import List
from collections import defaultdict
from z_algorithm import z_algorithm

def bm(txt: str, pat: str):
    """
    Inputs:
    - txt[0..m]: Where to search for valid pat matches
    - pat[0..n]: What we are finding in txt.

    Outputs:
    - res: A result array containing indexes of the start of valid occurences of pat found in txt 

    Complexity:
    - Time: O(n+m) worst case. O(n/m) average case.

    """
    res = []
    if len(txt) < len(pat):
        return res
    n = len(txt)
    
    # Pre-processing
    bc = create_bc_array() # Bad Character
    gs = create_gs_array() # Good Suffix
    mp = [0] * n # Matching Prefix




    # Search

    return res

def create_bc_array(pat: str) -> dict:
    bc = defaultdict(List[int])

    for idx, char in enumerate(pat):
        bc[char].append(idx)

    return bc

def create_gs_array(pat: str) -> List:
    m = len(pat)
    gs = [0] * (m + 1)
    z = z_algorithm(pat[::-1])[::-1]

    for i in range(m - 1): # Don't want to compare the last value.
        j = m - z[i]
        gs[j] = i

    return gs

def create_mp_array(pat: str) -> List:
    m = len(pat)
    mp = [0] * (m + 1)
    z = z_algorithm(pat)[::-1]

    temp = [i for i in range(m)]
    print(temp)

    maxx = 0
    for i in range(m, -1, -1):
        maxx = max(z[i], maxx)
        mp[i] = maxx

    return mp

def binary_search(arr: List[int], target: int) -> int:
    """
    Implementation of binary search that finds the rightmost value smaller than target.
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid - 1 # modified to -1
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return high # modified to not return -1 
        

if __name__ == "__main__":
    arr = "acababacaba"
    res = create_mp_array(arr)
    print(res)