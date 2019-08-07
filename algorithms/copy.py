"""Basic module that only copies data, does not actually compress/decompress."""

import io
import dataclasses

from algorithms import utils
from .algorithm import Algorithm
from .compressed_file import CompressedFile

class Copy(Algorithm):
    """Copy data directly, no actual compression."""

    @classmethod
    def compress(self, metadata):
        data = utils.read(metadata.input_path)
        compressed_file = CompressedFile(metadata=dataclasses.asdict(metadata), data=data) 
        compressed_file.write(filepath=metadata.output_path)

    @classmethod
    def decompress(self, metadata):
        compressed_file = CompressedFile(metadata=None, data=None)
        compressed_file.read(metadata=metadata)
        utils.write(bytestream=compressed_file.data, filepath=compressed_file.output_path)
