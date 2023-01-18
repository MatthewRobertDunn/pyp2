from io import BufferedReader
from frameheader import MpegVersion, LayerVersion,ChannelMode, FrameHeader
import struct

FRAME_SYNC =    0b11111111111000000000000000000000
MPEG_VERSION =  0b11 << 19
LAYER_VERSION = 0b11 << 17
BITRATE_INDEX = 0b1111 << 12
SAMPLING_RATE_INDEX = 0b11 << 10
PADDING = 0b1 << 9;
CHANNEL_MODE = 0b11 << 6

#todo, others
BitRateIndex = {
    MpegVersion.Version10: {
        LayerVersion.Layer2: {
            0: -1,
            1: 32,
            2: 48,
            3: 56,
            4: 64,
            5: 80,
            6: 96,
            7: 112,
            8: 128,
            9: 160,
            10: 192,
            11: 224,
            12: 256,
            13: 320,
            14: 384
        }
    }
}

SamplingRateIndex = {
    MpegVersion.Version10: {
            0: 44100,
            1: 48000,
            2: 32000,
            3: -1
    }
}


#Reads an mpeg audio frame header from a file stream
def read_header(f: BufferedReader) -> FrameHeader:
    result = FrameHeader()
    header = struct.unpack('>I', f.read(4))[0]
    print(format(header, 'b'))
    
    #mpeg header
    is_mpeg_header = header & FRAME_SYNC == FRAME_SYNC
    if not is_mpeg_header:
        raise "Is not a valid frame header"

    #mpeg version
    mpeg_version = (header & MPEG_VERSION) >> 19
    result.mpeg_version = MpegVersion(mpeg_version)
    
    #layer version
    layer_version = (header & LAYER_VERSION) >> 17
    result.layer_version = LayerVersion(layer_version)

    #bitrate
    bitrate_index = (header & BITRATE_INDEX) >> 12
    bit_rate = BitRateIndex[result.mpeg_version][result.layer_version][bitrate_index]
    result.bit_rate = bit_rate

    #sampling rate
    sampling_rate_index = (header & SAMPLING_RATE_INDEX) >> 10
    sampling_rate = SamplingRateIndex[result.mpeg_version][sampling_rate_index]
    result.sampling_rate = sampling_rate

    #padding
    padding = (header & PADDING == PADDING)
    result.padding = padding
    
    #channel mode
    channel_mode = (header & CHANNEL_MODE) >> 6
    result.channel_mode = ChannelMode(channel_mode)

    return result
