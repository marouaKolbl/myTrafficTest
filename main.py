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
            date_value = pd.to_datetime(new_dataframe.loc[
                                               (new_dataframe[DataInfo.WEEKDAY_ID.value] == weekday) &
                                               (new_dataframe[DataInfo.SHOPPING_CENTER_ID.value] ==
                                                shopping_center)][DataInfo.DEVICE_LOCAL_DATE.value]).dt.date
            new_weekday = pd.DataFrame({'device_local_date': weekDay_value.values, 'date': date_value.values},
                                       index=weekDay_value)
            grouper = new_weekday.groupby([pd.Grouper(freq='1Min'), 'date'])
            df = grouper.count().unstack(fill_value=0)
            flow_matrice = np.array(df.values, dtype=np.float)
            statring_flow = flow_matrice
            time_array = df['device_local_date'].index.time.astype(str)
            fig, axs = plt.subplots(figsize=(12, 10))
            # for i, key in enumerate(df.keys()):
            # #     # print(flow_matrice[i, 0])
            # #     # print(df['device_local_date'].index.time.astype(str))
            #     starting = np.insert(flow_matrice[:-1, i], 0,
            #                          flow_matrice[0, i])
            #     statring_flow[:, i] = flow_matrice[:, i]-starting
            #     plt.plot(time_array,
            #              flow_matrice[:, i]-starting, marker="o", label=key[1])
            #     # plt.plot(time_array,
            #     #          flow_matrice[:, i], marker="o", label=key[1])
            # flow_matrice = flow_matrice
            # input_flow = flow_matrice - statring_flow
            plt.plot(time_array,
                     np.mean(flow_matrice, axis=1))
            from scipy.signal import find_peaks
            peaks, _ = find_peaks(np.mean(flow_matrice, axis=1), height=0)
            plt.plot(peaks, np.mean(flow_matrice, axis=1)[peaks], "x")
            time_peaks = time_array[peaks]
            time_opening = time_peaks[np.mean(flow_matrice, axis=1)[peaks] > 1][0]
            print(time_opening)

            kernel_size = 10
            kernel = np.ones(kernel_size) / kernel_size
            data_convolved_20 = np.convolve(np.nanmean(flow_matrice, axis=1), kernel, mode='same')
            # plt.plot(time_array,
            #          data_convolved_20, marker="*")

            axs.set_xticklabels(time_array, rotation=45)
            fig.savefig(os.path.join("output", shopping_center + "_weekDay_" + str(weekday) + ".png"))
            # print(df.values)
            # print(grouper.count().keys())
            # print(grouper.count()['device_local_date'].index.time.astype(str))
            # print(grouper.count()['device_local_date'].values)
            # fig, axs = plt.subplots(figsize=(12, 4))
            # starting = np.insert(grouper.count()['device_local_date'].values[:-1], 0, grouper.count()['device_local_date'].values[0])
            # print(starting)
            # plt.plot(grouper.count()['device_local_date'].index.time.astype(str),
            #          np.subtract(grouper.count()['device_local_date'].values, starting),
            #          marker="o", label="PMF")
            #
            # axs.set_xticklabels(grouper.count()['device_local_date'].index.time.astype(str), rotation=45)
            # fig.savefig(os.path.join("output", shopping_center + "_weekDay_" + str(weekday) + ".png"))


if __name__ == '__main__':
    main()
