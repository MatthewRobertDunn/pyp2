#Structure shared by all mpeg versions ``
from typing import List


class ChannelAllocationBits:
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


class BitAllocationRow:
    '''
        Row in the allocation table
        allocation_bits: Number of bits used to describe how many bits per sample
        sample_bits: Number of bits to describe a sample for a given configuration of allocation_bits 
    '''

    def __init__(self, allocation_bits: int, sample_bits: List[int]) -> None:
        self.allocation_bits = allocation_bits
        self.sample_bits = [ChannelAllocationBits(bit) for bit in sample_bits]

BitAllocationTable = List[BitAllocationRow]
