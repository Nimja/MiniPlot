# Install
This expects you to have python 3 installed on your OS of choice.

Instructions are for Linux/OSX

## Running in VirtualEnv
Start a virtual environment:
```bash
python3 -m venv venv
source ./venv/bin/activate
```

## Install dependencies
```bash
pip install -r requirements.txt
```

# Configuring
Look through the config file: `config.conf` and edit any settings you like.

## Reader
By default, the "fake" reader is configured, which generates random data.

Readers generate one long list of data, that will be handled by the writer.

## Input file
Make sure you place the input file in the input folder and configure it in the `config.conf`

Since the bit reader will literally read bits/bytes, you could use ANY file as input.

## (Optional) Generating test data
It's possible to generate (large) datasets for import (on Linux/OSX).

With the example of our large data (155m datapoints), of 2 bits (values of 0-3), we can calulate how many bytes we want the file to be.

155,000k / 8(bits in a byte) * 2(desires bits) = 38,750k

This will take a while as it is generating a file of random content, of 38 megabytes.

```bash
dd if=/dev/urandom of=input/test.data bs=1 count=38750000
```

# Running
```bash
python3 main.py
```
You will see output as the file is read in and the PNG is written.

## Example output
```bash
Step 1 - Reading...
Generating RANDOM data with length 654321 of 2 bits
...  95.0% - 1.03s
Step 1 - Done: Length:  654321
Step 2 - Writing...
Generating PNG - width: 810, height: 808, colors: 5
PNG exported: output/test.png
Step 2 - Done!
```

## Notes
This process can take a while. For the intended purpose (visualizing DNA), it would take about 10 minutes to read in the data and a few more to generate the 12k x 12k image.

However, as far as I can tell, it works just fine!