from typing import ByteString
from frameheader import MpegVersion, LayerVersion,ChannelMode, FrameHeader




class Frame:
    def __init__(self, frame_header: FrameHeader, data: ByteString)-> None:
        self.frame_header = frame_header
        self.data = data

    @property
     def age(self):
     print("getter method called")
     return self._age
