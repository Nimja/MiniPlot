import random

from .reporter import Reporter
# This generates fake data, which is faster than reading real data. Can be useful for testing.


# How many updates we want, 100 would be every percentage. 4 would be every 25%.
UPDATES = 20


def read(config, file_name):
    """
    Randomly generate (fake) data. File_name is unused, but there for consistency.

    :param config: dict - Config values from the config file.
    :param file_name: string - Unused for the fake reader.
    """
    # Get bit length, default to 1 byte.
    bit_length = int(config.get('bits', 8))

    # Generate length.
    generate_length = int(config.get('length', 1000))
    reporter = Reporter(generate_length, updates=UPDATES)


    print("Generating RANDOM data with length {} of {} bits".format(generate_length, bit_length))
    result = []
    max_value = 2 ** bit_length - 1
    for i in range(generate_length):
        result.append(random.randint(0, max_value))
        reporter.report(len(result))

    return result