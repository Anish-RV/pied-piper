"""Yeehaw."""
import argparse
from algorithms.copy import Copy
from algorithms.huffman import Huffman
from algorithms.metadata import Metadata


def set_up_parser():
    """Set up the parser."""
    parser = argparse.ArgumentParser(description='Pied Piper')
    parser.add_argument('-i', '--inputpath', required=True)
    parser.add_argument('-a', '--algorithm', default='copy')
    parser.add_argument('-o', '--outputpath', default=None)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d', '--decompress', action='store_true')
    group.add_argument('-c', '--compress', action='store_true')
    # parser.add_argument('-v', '--verbose', choices=['DEBUG', 'CRITICAL', 'INFO'], default='DEBUG')
    return parser

# def setup_logging(args):
#     """Set up logging for our tool."""
#     if args.verbose:
#         logging = args.verbose


def call_module(metadata):
    """Call the approriate compression/decompression algorithm."""
    algorithm = metadata.algo_type
    print(algorithm)
    if algorithm == 'copy':
        alg_class = Copy
    if algorithm == 'huffman':
        alg_class = Huffman()
    if (args.compress):
        alg_class.compress(metadata)
    else:
        metadata.compress = False
        alg_class.decompress(metadata)


if '__main__' == __name__:
    parser = set_up_parser()
    args = parser.parse_args()
    file_metadata = Metadata(input_path=args.inputpath,
                             output_path=args.outputpath,
                             extension=None,
                             algo_type=args.algorithm,
                             compress=args.compress)
    call_module(file_metadata)
