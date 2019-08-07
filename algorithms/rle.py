import io
import dataclasses

from algorithms import utils
from .algorithm import Algorithm
from .compressed_file import CompressedFile

class RLE(Algorithm):
    @classmethod
    def compress(self, metadata):
        data = utils.read(metadata.input_path)
        compressed_data = ''
        length = len(data)
        num = 0
        for i, byte in enumerate(data[:-1]):
            if byte == data[i+1]:
                num += 1
            else:
                num += 1
                compressed_data += str(num)
                compressed_data += chr(byte)
                num = 0

        if num == 0:
            compressed_data += chr(data[-1])
        else:
            num += 1
            compressed_data += str(num)
            compressed_data += chr(data[-1])

        compressed_file = CompressedFile(metadata=dataclasses.asdict(metadata), data=bytes(compressed_data, 'utf-8'))
        compressed_file.write(filepath=metadata.output_path)

    @classmethod
    def decompress(self, metadata):
        pass
    