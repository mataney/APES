import argparse

from run_apes import apes
from run_rouge import rouge

def main():
    parser = argparse.ArgumentParser(description='Answering to questions')
    parser.add_argument('--preds_file', required=True, type=str)
    parser.add_argument('--targets_file', required=True, type=str)
    parser.add_argument('--questions_mapping_path', required=True, type=str)
    parser.add_argument('--filenames_path', required=True, type=str)
    args = parser.parse_args()

    apes(args.preds_file, args.filenames_path, args.questions_mapping_path)
    rouge(args.preds_file, args.targets_file)


if __name__ == "__main__":
   main()