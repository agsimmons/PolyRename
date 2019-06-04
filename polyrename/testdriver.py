import argparse
from pathlib import Path

from transformation import TRANSFORMATIONS


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='+')
    return parser.parse_args()


def main():
    args = parse_args()
    file_sequence = [Path(file) for file in args.files if Path(file).exists()]

    print('Choose a transformation:')
    for i, tranformation in enumerate(TRANSFORMATIONS):
        print('{}) {}'.format(i, tranformation.schema['metadata']['name']))

    # Ask for selection input
    choice = None
    while choice not in range(len(TRANSFORMATIONS)):
        try:
            choice = int(input('Selection: '))
        except ValueError:
            pass

    # Gather arguments for selected transformation
    transformation_class = TRANSFORMATIONS[choice]
    transformation_args = []
    for option in transformation_class.schema['options']:
        input_prompt = '{} ({}):'.format(option['name'], option['description'])
        choice = None
        while not choice:
            try:
                choice = option['datatype'](input(input_prompt))
            except ValueError:
                print('Invalid input!')
        transformation_args.append(choice)

    # Create transformation with selected arguments
    tranformation = transformation_class(file_sequence, *transformation_args)
    transformed_file_sequence = tranformation.resolve()
    for file_pairs in zip(file_sequence, transformed_file_sequence):
        print('{} -> {}'.format(*file_pairs))


if __name__ == '__main__':
    main()
