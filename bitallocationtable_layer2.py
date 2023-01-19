from enum import Enum
from typing import List
from bitallocationtable import BitAllocationRow

'''
Number of bits to describe channel sample storage, followed by actual number of bits to store sample
Negative means 'grouped' samples. See mpeg spec
'''
BitAllocationTableRows = [
    BitAllocationRow(2, [0, -5, -7, 16]),
    BitAllocationRow(3, [0, -5, -7,  3, -10,  4,  5, 16]),
    BitAllocationRow(4, [0, -5, -7,  3, -10,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 16]),
    BitAllocationRow(4, [0, -5,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16]),
    BitAllocationRow(4, [0, -5, -7, -10,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15]),
    BitAllocationRow(3, [0, -5, -7, -10,  4,  5,  6,  9]),
    BitAllocationRow(4, [0, -5, -7,  3, -10,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14]),
    BitAllocationRow(2, [0, -5, -7,  3])
]

'''
The actual allocation lookup table. This is the only part of this useful to consumers of this module
One of these enum values needs to be chosen based on bitrate, sample rate, mpeg version.
'''

class AllocationTablesLayer2:
    high_rate_27_bands = [BitAllocationTableRows[x] for x in [3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]]
    high_rate_30_bands = [BitAllocationTableRows[x] for x in [3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]]
    low_rate_8_bands = [BitAllocationTableRows[x] for x in [4, 4, 5, 5, 5, 5, 5, 5]]
    # For mpeg2.5? don't think this gets used.
    lsf_30_bands = [BitAllocationTableRows[x] for x in [6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]],
