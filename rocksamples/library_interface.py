from math import *
from pathlib import Path
import numpy as np

from rocksamples import analyse
from rocksamples.comparison import open_file

input_files = ['sample_data/samples1.csv', 'sample_data/samples2.csv']
input_data = []

def main():

    # loading 2 data and weights files
    # data_files_directory = Path('sample_data')
    #
    # data_name1 = Path(data_files_directory/input_files[0])
    # data_name2 = Path(data_files_directory/input_files[1])
    # weights_data = Path(data_files_directory/'weights.csv')

    input_data1 = open_file(input_files[0])
    input_data2 = open_file(input_files[1])
    weights_data = open_file('sample_data/weights.csv')
    input_data = [input_data1, input_data2]
    # we should run from this method.
    analyse(input_data, weights_data, summary='d', analysis='y', threshold=5)

    return


if __name__ == '__main__':
    main()