# Install

This expects you to have python 3 installed.

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
Explain config file.


# (Optional) Generating test data
On Linux/Mac environments generating test data can be done with:

With data count of 4 (2 bits), we want 155m datapoints for testing. Bytes are 8 bits, so we can divided it by 4.
155000000 / 4 = 38750000

This file will be about 38 MegaBytes!

```bash
dd if=/dev/urandom of=input/test.data bs=1 count=38750000
```

# Running
```bash
python3 main.py
```