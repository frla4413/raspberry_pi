import os

def get_last_reading(filename):
    with open(filename, 'rb') as f:
        try:  # catch OSError in case of a one line file
            f.seek(-2, os.SEEK_END)
            while f.read(1) != b'\n':
                f.seek(-2, os.SEEK_CUR)
        except OSError:
            f.seek(0)
        last_reading = f.readline().decode()
    return last_reading

def get_last_dht11_reading(filename):
    last_reading = get_last_reading(filename)
