import configparser
import reader
import writer

reader_mapping = {
    'bit': reader.bit_reader,
    'fake': reader.fake_reader,
}
writer_mapping = {
    'png': writer.palette_png
}


# Parse config file.
config = configparser.ConfigParser()
config.read('config.conf')
options = config['options']

# Read options
data_size = int(options.get('count', 4))
input_file = options.get('input_file', 'input/test.data')
ouput_file = options.get('ouput_file', 'output/test.png')

reader_name = options.get('reader', 'bit')
if reader_name not in reader_mapping:
    raise Exception("Unknown reader selected: {}".format(reader_name))

writer_name = options.get('writer', 'png')
if writer_name not in writer_mapping:
    raise Exception("Unknown writer selected: {}".format(writer_name))

# Execute reader.
print("Step 1 - Reading...")
data = reader_mapping[reader_name].read(
    config['reader'],
    input_file
)
print("Step 1 - Done: Length: ", len(data))

# Execute writer.
print("Step 2 - Writing...")
writer_mapping[writer_name].write(
    config['writer_png'],
    data,
    ouput_file
)
print("Step 2 - Done!")