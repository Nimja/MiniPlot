import configparser
from writer import palette_png
from reader import bit_reader


# Parse config file.
config = configparser.ConfigParser()
config.read('config.conf')
options = config['options']

# Read options
data_size = int(options.get('count', 4))
input_file = options.get('input_file', 'input/test.data')
ouput_file = options.get('ouput_file', 'output/test.png')

# Execute reader.
data = bit_reader.read(config['bit_reader'], input_file)
print("Data read. Length: ", len(data))

# Execute writer.
print("Writing data.")
palette_png.write(config['palette_png'], data, ouput_file)
print("Done!")