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

## Input file
Make sure you place the input file in the input folder and configure it in the `config.conf`


## (Optional) Generating test data
Using the OS, it's possible to generate (large) datasets for import.

With data count of 4 (2 bits), we want 155m datapoints for testing. Bytes are 8 bits, so we can divided it by 4.
155000000 / 4 = 3,875,0000

This file will be about 38 MegaBytes!

```bash
dd if=/dev/urandom of=input/test.data bs=1 count=38750000
```

# Running
```bash
python3 main.py
```
You will see output as the file is read in and the PNG is written.
