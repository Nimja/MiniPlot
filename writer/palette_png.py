import png
import math

def write(config, data, file_name):
    # Get size and split up data.
    color_count = int(config.get('color_count', 1))
    width = int(config.get('width', 0))
    if not width:
        width = _get_dynamic_width(len(data))

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

    print("PNG exported:", file_name)

def _get_palette(color_count, config):
    """ From config to palette.
    """
    result = []
    for i in range(color_count):
        # Default to transparent color.
        color = config.get('color{}'.format(i), '0,0,0,0')
        # Convert into integers.
        color = list(map(int, color.split(',')))
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

def _get_dynamic_width(total):
    """
    Attempt to get width that is the closest to a square, rounded up on the first 2 digits.
    """
    square_root = math.sqrt(total)
    # Get number of digits.
    digits = math.ceil(math.log10(square_root))
    # Get multiplier that we want to use for rounding.
    multiplier = 10 ** max(digits - 2, 1)
    return math.ceil(square_root / multiplier) * multiplier