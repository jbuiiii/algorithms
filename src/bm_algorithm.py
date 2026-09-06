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
from src.z_algorithm import z_algorithm

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
    n = len(txt)
    m = len(pat)

    if n < m:
        return res
    
    # Pre-processing
    bc = create_bc_array(pat=pat) # Bad Character
    gs = create_gs_array(pat=pat) # Good Suffix
    mp = [0] * n # Matching Prefix

    # Search
    skip = 0
    i = 0

    while i <= n - m:
        j = m - 1

        # Start comparisons from right to left.
        while j >= skip: # Ensures unnecessary comparisons are not repeated.
            if pat[j] == txt[i + j]:
                j -= 1
            else:
                break

        if j < skip:
            res[i] = 1

        shift = max(bc[i], gs[i], mp[i])

        # TODO: Implement shifting optimisation.
        
    return res

def create_bc_array(pat: str) -> List[List[int]]:
    alphabet = sorted(set(pat))

    res = [[-1] * len(pat) for _ in range(len(alphabet))]

    for char in range(len(alphabet)):
        last_seen = -1
        for i in range(len(pat)):
            if pat[i] == alphabet[char]:
                last_seen = i
            res[char][i] = last_seen
 
    return res

def create_gs_array(pat: str) -> List:
    m = len(pat)
    gs = [0] * (m)
    z = z_algorithm(pat[::-1])[::-1]

    for i in range(m - 1): # Don't want to compare the last value.
        j = m - z[i]
        if j != m:
            gs[j] = i + 1

    return gs

def create_mp_array(pat: str) -> List:
    m = len(pat)
    mp = [0] * m
    z = z_algorithm(pat)
    longest = 0

    for i in range(m - 1, 0, -1):
        longest = max(longest, z[i])
        mp[i] = longest
    mp[0] = m

    return mp

if __name__ == "__main__":
    pat = "abaaabacbaabaaab"
    print(create_mp_array(pat))
    