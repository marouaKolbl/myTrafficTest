# This is a sample Python script.
import argparse
import pandas as pd
import numpy as np

from preprocessings import load_data, get_weekday, DataInfo


def create_parser():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('-input_file',
                           type=str,
                           help='input data path',
                           default="resources/data.csv",
                           required=True)
    return my_parser


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    args = create_parser().parse_args()
    dataframe = load_data(args.input_file)
    print(dataframe.keys())
    new_dataframe = get_weekday(dataframe)
    shopping_center_array = np.array(new_dataframe[DataInfo.SHOPPING_CENTER_ID.value])
    weekday_array = np.array(new_dataframe[DataInfo.WEEKDAY_ID.value])
    print(np.unique(weekday_array))
    print(np.unique(shopping_center_array))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
