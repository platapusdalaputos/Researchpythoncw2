import pytest
import math
from src.main import open_file
from pathlib import Path
from pytest import raises

from src.rocksamples import algorithm_x, algorithm_y


def test_algorithm_x_missing_data_values():
    data_files_directory = Path('tests/test_files')
    data_name1  = Path(data_files_directory / 'data1_missing_values.csv')
    data_name2 = Path(data_files_directory / 'data2_missing_values.csv')
    weights_data = Path(data_files_directory / 'weights_missing_values.csv')

    data1 = open_file(data_name1)
    data2 = open_file(data_name2)
    weights = open_file(weights_data)

    # output should be 𝑑 = 1⋅|1−1.1|+0.5⋅|2−2|+2⋅|3−5| = 4.1
    expected_d = 1*abs(1-1.1)+ 0.5*abs(2-2)+ 2*abs(3-5)
    actual_d = algorithm_x(data1, data2, weights)
    assert expected_d == actual_d


def test_algorithm_y_missing_data_values():
    data_files_directory = Path('tests/test_files')
    data_name1  = Path(data_files_directory / 'data1_missing_values.csv')
    data_name2 = Path(data_files_directory / 'data2_missing_values.csv')
    weights_data = Path(data_files_directory / 'weights_missing_values.csv')

    data1 = open_file(data_name1)
    data2 = open_file(data_name2)
    weights = open_file(weights_data)

    # w =     1,   10,  0.5,  2, 2
    # data1 = 1,   nan,  2,   3, 2.6
    # data2 = 1.1, 3.5, 2,   5, nan
    expected_d = math.sqrt(1*(1-1.1)**2+0.5*(2-2)**2+ 2*(3-5)**2)

    actual_d = algorithm_y(data1, data2, weights)
    assert expected_d == actual_d