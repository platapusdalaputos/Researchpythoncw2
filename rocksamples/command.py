from rocksamples.comparison import open_file

from rocksamples import analyse
from argparse import ArgumentParser


def process():
    parser = ArgumentParser(description="Generate appropriate greetings")

    parser.add_argument('data_file1',  help='first data file') #default='sample_data/samples1.csv',
    parser.add_argument('data_file2',  help='second data file') #default='sample_data/samples2.csv',
    parser.add_argument('--weights', default='', help='weight files for features, if not, each feature weight 1')
    parser.add_argument('--analysis', default='x', help='algorithm for comparision data, default x')
    parser.add_argument('--summary', default='d', help='summary method for comparision results, default d-index')
    parser.add_argument('--threshold', default=0, type=int, help='the threshold to compare data difference')
    # parser.add_argument('--config', help ='')
    arguments = parser.parse_args()

    # open yamlpath
    # yaml.load(yamlpath)
    input_data1 = open_file(arguments.data_file1)
    input_data2 = open_file(arguments.data_file2)
    input_data = [input_data1 , input_data2]
    print(analyse(input_data, arguments.weights, arguments.analysis,
                  arguments.summary, arguments.threshold))


if __name__ == "__main__":
    process()