import png
import math

def write(config, data, file_name):
    # Get size and split up data.
    color_count = int(config.get('color_count', 1))
    width = int(config.get('width', 1))
    height = math.ceil(len(data) / width)
    chunk_data = _chunks(data, width, int(config.get('background', 0)))
    # Print nice information.
    print("Generating PNG - width: {}, height: {}, colors: {}".format(width, height, color_count))

    # Setup PNG.
    w = png.Writer(
        width, # Width
        height, # Height
        palette=_get_palette(color_count, config),
        bitdepth=_get_bit_depth(color_count)
    )
    # Write PNG.
    with open(file_name, 'wb') as f:
        w.write(f, chunk_data)

def _get_palette(color_count, config):
    """ From config to palette.
    """
    result = []
    for i in range(color_count):
        color = config.get('color{}'.format(i), '0,0,0')
        color = color.split(',')
        color = list(map(int, color))
        result.append(color)
    return result

def _get_bit_depth(color_count):
    """ Return palette bit depth, one of 1, 2, 4 or 8.
    """
    for i in [1, 2, 4, 8]:
        if color_count <= 2**i:
            return i


def _chunks(lst, width, bg):
    """ Yield successive n-sized chunks from lst. """
    # Padd list with background index, for safety.
    height = math.ceil(len(lst) / width)
    padding = height * width - len(lst)
    if padding > 0:
        lst.extend([bg] * padding)
    # Yield chunks of exactly "width" size.
    for i in range(0, len(lst), width):
        yield lst[i:i + width]
