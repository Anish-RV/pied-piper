from dataclasses import dataclass
import json
import base64
from pathlib import Path

import exceptions

@dataclass
class CompressedFile:
    metadata: dict
    data: bytes

    # @classmethod
    def read(self, metadata):
        with open(metadata.input_path, 'r') as fp:
            compressed_file = json.load(fp=fp)

        if 'metadata' not in compressed_file or 'data' not in compressed_file:
            raise exceptions.FileFormatError

        input_path = Path(metadata.input_path)
        output_path = Path(input_path.stem)
        self.output_path = output_path.with_suffix(
            compressed_file['metadata']['extension']
        )
        self.metadata = compressed_file['metadata']
        self.data = compressed_file['data'].encode('utf-8')

    def write(self, filepath):
        compressed_file = {
            'metadata': self.metadata,
            'data': self.data.decode('utf8')
        }
        with open(filepath, 'w') as fp:
            json.dump(obj=compressed_file, fp=fp)
