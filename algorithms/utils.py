"""Utilities for Algorithm Modules."""

# TODO: Move to top-level utils
def read(filepath):
    with open(filepath, 'rb') as fp:
        data = fp.read()
    return data

def write(bytestream, filepath):
    with open(filepath, 'wb') as fp:
        fp.write(bytestream)
