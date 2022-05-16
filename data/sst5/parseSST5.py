import os

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

if __name__ == "__main__":
    with open(f'{ROOT_DIR}/data/sst5/train.txt', 'r') as sst:
        print()