from bitstring import ConstBitStream, ReadError
from .reporter import Reporter

# How many updates we want, 100 would be every percentage. 4 would be every 25%.
UPDATES = 100


def read(config, file_name):
    """
    Read binary file into an array of unsigned integers.

    :param config: dict - Config values from the config file.
    :param file_name: string - The file we read from, using bitstream.
    """
    # Get bit length, default to 1 byte.
    bit_length = int(config.get('bits', 8))
    print("Reading file {} - Splitting up in chunks of {} bits.".format(file_name, bit_length))
    stream = ConstBitStream(filename=file_name)

    print("Starting to read...")
    reporter = Reporter(int(len(stream) / bit_length), updates=UPDATES)

    return _read_read(stream, bit_length, reporter)
    # return _read_cut(stream, bit_length)


def _read_cut(stream, bit_length, reporter):
    """
    Testing showed that this is 3 times slower than using read. Shame.
    """
    result = []
    for chunk in stream.cut(bit_length):
        if chunk is None:
            break
        result.append(chunk.uint)
        reporter.report(len(result))
    return result

def _read_read(stream, bit_length, reporter):
    """
    Currently the faster way of reading.
    """
    bform = 'uint:{}'.format(bit_length)

    result = []
    while True:
        try:
            result.append(stream.read(bform))
            reporter.report(len(result))
        except ReadError:
            break
    return result
