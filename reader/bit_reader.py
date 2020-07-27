from bitstring import ConstBitStream, ReadError
# This will read a binary stream from a file, interpreting it as X bits.


def read(config, file_name):
    # Get bit length, default to 1 byte.
    bit_length = int(config.get('bits', 8))
    print("Reading file {} - Splitting up in chunks of {} bits.".format(file_name, bit_length))

    stream = ConstBitStream(filename=file_name)

    result = []
    for chunk in stream.cut(bit_length):
        if chunk is None:
            break
        result.append(chunk.uint)
    return result
