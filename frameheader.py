#Contains metadata and structures relating to mpeg frame header

from enum import Enum

class ChannelMode(Enum):
    Stereo = 0b00
    JointStereo = 0b01
    DualChannel = 0b10
    SingleChannel = 0b11

class MpegVersion(Enum):
    Version25 = 0b00
    Reserved = 0b01
    Version20 = 0b10
    Version10 = 0b11

class LayerVersion(Enum):
    Reserved = 0b00
    Layer3 = 0b01
    Layer2 = 0b10
    Layer1 = 0b11


class FrameHeader:
    def __init__(self) -> None:
        self.mpeg_version = MpegVersion.Reserved,
        self.layer_version = LayerVersion.Reserved,
        self.bit_rate = 0,
        self.sampling_rate = 0,
        self.channel_mode = ChannelMode.Stereo
        self.padding = False
        pass
