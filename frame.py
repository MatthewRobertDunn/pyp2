from typing import ByteString, List
from bitallocationtable import BitAllocationTable
from bitallocationtable_layer2 import AllocationTablesLayer2
from frameheader import FrameHeader

class Frame:
    def __init__(self, frame_header: FrameHeader, data: ByteString)-> None:
        self.frame_header = frame_header
        self.data = data

    '''
    Returns the allocation lookup table for the current frame
    '''
    @property
    def bit_allocation_table(self) -> BitAllocationTable:
        return AllocationTablesLayer2.high_rate_30_bands  #todo: support more.
