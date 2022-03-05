"""Preprocessing functions."""
import enum
from datetime import datetime

import pandas as pd


class DataInfo(enum.Enum):
    """Enum class for data information list."""
    DEVICE_ID = "device_hash_id"
    DEVICE_LOCAL_DATE = "device_local_date"
    SHOPPING_CENTER_ID = "shopping_center_id"
    WEEKDAY_ID = "weekday_id"
    TIMESTAMP = "timestamp"
    SLOT = "slot"


def load_data(filename: str) -> pd.DataFrame:
    """Load data."""
    return pd.read_csv(filename, sep=',')


def get_weekday(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Get Week day"""
    week_day = []
    timestamps = []
    for i, data in dataframe.iterrows():
        date_format = datetime.strptime(data[DataInfo.DEVICE_LOCAL_DATE.value].split(" ")[0], '%Y-%m-%d')
        week_day.append(date_format.weekday())
        date_format = datetime.strptime(data[DataInfo.DEVICE_LOCAL_DATE.value].split(" ")[1], '%H:%M:%S')
        timestamps.append(date_format.timestamp())
    dataframe[DataInfo.WEEKDAY_ID.value] = week_day
    # dataframe[DataInfo.TIMESTAMP.value] = timestamps

    return dataframe