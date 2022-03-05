# This is a sample Python script.
import argparse
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
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
    for weekday in np.unique(weekday_array):
        for shopping_center in np.unique(shopping_center_array):

            weekDay_value = pd.to_datetime(new_dataframe.loc[
                                               (new_dataframe[DataInfo.WEEKDAY_ID.value] == weekday) &
                                               (new_dataframe[DataInfo.SHOPPING_CENTER_ID.value] ==
                                                shopping_center)][DataInfo.DEVICE_LOCAL_DATE.value]).apply(
                lambda x: x.replace(day=1).replace(month=3).replace(year=2022))

            new_weekday = pd.DataFrame({'device_local_date': weekDay_value.values},
                                       index=weekDay_value)
            grouper = new_weekday.groupby([pd.Grouper(freq='15Min')])
            print(grouper.count().keys())
            print(grouper.count()['device_local_date'].index.time.astype(str))
            print(grouper.count()['device_local_date'].values)
            fig, axs = plt.subplots(figsize=(12, 4))
            plt.plot(grouper.count()['device_local_date'].index.time.astype(str),
                     grouper.count()['device_local_date'].values,
                     marker="o", label="PMF")

            axs.set_xticklabels(grouper.count()['device_local_date'].index.time.astype(str), rotation=45)
            fig.savefig(os.path.join("output", shopping_center + "_weekDay_" + str(weekday) + ".png"))


if __name__ == '__main__':
    main()
