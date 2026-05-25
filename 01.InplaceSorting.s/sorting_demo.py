#!/usr/bin/env -S python3
"""
Sortings demo
"""
from random import shuffle
import sys
from comp_swap_container import CompSwapList
import sortings

if __name__ == "__main__":
    if len(sys.argv) > 1:
        sizes = [int(sys.argv[1])]
    else:
        sizes = [10, 100, 1000]

    for n in sizes:
        arr = list(range(n))
        shuffle(arr)

        # bubble_sort
        data = CompSwapList(arr)
        sortings.bubble_sort(data)
        print(n, data.comps, data.swaps)

        # quick_sort
        data = CompSwapList(arr)
        sortings.quick_sort(data)
        print(n, data.comps, data.swaps)
