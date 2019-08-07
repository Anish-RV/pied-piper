"""Metadata class."""
import pathlib
from typing import Dict
from dataclasses import dataclass, field
from pathvalidate import ValidationError, validate_filepath
from .constants import ALGO_LIST


@dataclass
class Metadata:
    """Metadata class."""

    input_path: str
    output_path: str
    extension: str
    algo_type: str
    compress: bool = True
    key: Dict = field(default_factory=dict)

    def __post_init__(self):
        """Initization."""
        if not self.output_path or not self.compress:
            self.output_path = self.input_path
        self.validate_data()
        if self.compress:
            self.output_path += '.pp'
            self.extension = pathlib.Path(self.input_path).suffix
        else:
            self.output_path = self.output_path.replace('.pp', '')

    def validate_data(self):
        """Validate input."""
        if (self.algo_type not in ALGO_LIST):
            self.algo_type = 'copy'
        try:
            validate_filepath(self.input_path)
        except ValidationError as ve:
            print('Import file path' + ve)
            raise ve
        try:
            validate_filepath(self.output_path)
        except ValidationError as ve:
            print('Output file path' + ve)
            raise ve
