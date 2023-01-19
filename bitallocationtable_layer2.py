from enum import Enum
from typing import List


class SampleBits:
    '''
        Describes how a channel sample is stored
        bits: number of bits used to describe a sample, if bits < 0 then it implies grouped, see mpeg spec
    '''

    def __init__(self,  bits: int) -> None:
        if bits < 0:
            self.grouped = True
            self.bits = -bits
        else:
            self.grouped = False
            self.bits = bits


class AllocationRow:
    '''
        Row in the allocation table
        allocation_bits: Number of bits used to describe how many bits per sample
        sample_bits: Number of bits to describe a sample for a given configuration of allocation_bits 
    '''

    def __init__(self, allocation_bits: int, sample_bits: List[int]) -> None:
        self.allocation_bits = allocation_bits
        self.sample_bits = [SampleBits(bit) for bit in sample_bits]


'''
Number of bits to describe channel sample storage, followed by actual number of bits to store sample
Negative means 'grouped' samples. See mpeg spec
'''
AllocationTableRows = [
    AllocationRow(2, [0, -5, -7, 16]),
    AllocationRow(3, [0, -5, -7,  3, -10,  4,  5, 16]),
    AllocationRow(4, [0, -5, -7,  3, -10,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 16]),
    AllocationRow(4, [0, -5,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16]),
    AllocationRow(4, [0, -5, -7, -10,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15]),
    AllocationRow(3, [0, -5, -7, -10,  4,  5,  6,  9]),
    AllocationRow(4, [0, -5, -7,  3, -10,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14]),
    AllocationRow(2, [0, -5, -7,  3])
]

'''
The actual allocation lookup table. This is the only part of this useful to consumers of this module
One of these enum values needs to be chosen based on bitrate, sample rate, mpeg version.
'''


class AllocationTable(Enum):
    high_rate_27_bands = [AllocationTableRows[x] for x in [3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]]
    high_rate_30_bands = [AllocationTableRows[x] for x in [3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]]
    low_rate_8_bands = [AllocationTableRows[x] for x in [4, 4, 5, 5, 5, 5, 5, 5]]
    # For mpeg2.5? don't think this gets used.
    lsf_30_bands = [AllocationTableRows[x] for x in [6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]],
