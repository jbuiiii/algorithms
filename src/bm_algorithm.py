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
    alphabet = sorted(set(pat))
    character_index = {char: idx for idx, char in enumerate(alphabet)}
    bc = create_bc_array(pat=pat) # Bad Character
    gs = create_gs_array(pat=pat) # Good Suffix
    mp = create_mp_array(pat=pat) # Matching Prefix


    # Search
    i = 0
    while i <= n - m:
        j = m - 1 # where the searching begins from inside pat
        while j >= 0 and pat[j] == txt[i + j]:
            j -= 1

        if j < 0: # if the search is successful
            res.append(i)
            # shift can only be from matched prefix if search is successful
            shift = m - mp[1] if m > 1 else 1
        else:
            # calculate all shifts

            # bc
            bad_char = txt[i + j]
            if bad_char in character_index:
                last_occ = bc[character_index[bad_char]][j]
            else:
                last_occ = -1
            bc_shift = j - last_occ

            # gs + mp
            if j + 1 < m: # check if there is any matched chars to use for gs + mp
                gs_shift = gs[j + 1]
                mp_shift = m - mp[j + 1]
            else: 
                gs_shift, mp_shift = 1, 1
            
            shift = max(1, bc_shift, gs_shift, mp_shift)

        i += shift
        
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
    z = _z(pat[::-1])[::-1]

    for i in range(m - 1): # Don't want to compare the last value.
        j = m - z[i]
        if j != m:
            gs[j] = i + 1

    return gs

def create_mp_array(pat: str) -> List:
    m = len(pat)
    mp = [0] * m
    z = _z(pat)
    longest = 0

    for i in range(m - 1, 0, -1):
        if z[i] == m - i:
            longest = z[i]
        mp[i] = longest
    mp[0] = m

    return mp

# taken from z_algorithm.py to mitigate import errors.
def _z(txt: str) -> List[int]:
    """
    Inputs:
    - txt: String to perform the Z-algorithm on. 
    
    Outputs:
    - List of Z-values = For a string str[1 ... n], define Z_i (for each position i > 1 in str) as the length of the longest 
    substring starting at position i of str that matches its prefix (i.e. str[i . . .i+Zi-1] = str[1 . . .Zi]). The set of 
    values {Zi, for 2 ≤ i ≤ n} for the string str[1...n] are what we refer to as its Z-values.
    
    Complexity:
    - Time: O(n), where n = len(txt)
    """
    z = [0] * len(txt)
    L, R = 0, 0

    for k in range(1, len(txt)):

        # Case 1
        if k > R:
            i = k
            while i < len(txt) and txt[i] == txt[i - k]: # Avoiding for loops avoids UnboundIndexErrors
                i += 1
            z[k] = i - k
            if z[k] > 0:
                L, R = k, i

        # Case 2: k <= r, i.e. exists inside a z-box
        else: # if k <= R
            # Case 2A
            if z[k - L] < R - k:
                z[k] = z[k - L]
                # L, R are unchanged.
            
            # Case 2B
            else:
                # Explicit comparisons are needed as the z-box does not give enough information.
                i = R
                while i < len(txt) and txt[i] == txt[i - k]:
                    i += 1
                z[k] = i - k
                # No if statement required, as this had to past the existing z-box.
                L, R = k, i

    return z

    