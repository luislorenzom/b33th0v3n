import logging

from src.arguments import parser, args
from src.dataset import get_datasets
from src.io.load import load_songs_from_csv, load_songs_from_folder
from src.constants import DEFAULT_OUTPUT
from src.io.save import save_output
from src.refactor import refactor

if __name__ == '__main__':
    # Set Logging
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

    # Download datasets
    if args.get_datasets_switch:
        get_datasets()

    # Get input args and show help
    if args.files_songs is not None:
        input_files = load_songs_from_csv(args.files_songs)
    elif args.music_folder is not None:
        input_files = load_songs_from_folder(args.music_folder)
    else:
        parser.print_help()
        exit()

    # Get output args
    output_file = args.output if args.output is not None else DEFAULT_OUTPUT

    # Run refactor recommendation and save results
    save_output(refactor(input_files), output_file)
