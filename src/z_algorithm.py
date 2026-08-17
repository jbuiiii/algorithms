# Author: jbuiiii
# Date created: 5/08/2026

"""
Implementation of Z-algorithm, which calculates an array containing Z_i values starting from i = 2. 

This can be extended into pattern matching by placing the pattern at the start of the string followed by a delimiter,
and then the text to pattern match with. Any suffixes found that are equal to the length of the pattern are valid matches.
"""
from typing import List, Tuple

def z_algorithm(txt: str) -> List[int]:
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
