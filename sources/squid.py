from typing import List

from sources import source
import iplogs

import pandas as pd


class Squid(source.Source):
    def __init__(self, files: List[str]):
        """
        create dataframe from given files
        """
        self.files = files
        self.headers = ["timestamp", "size", "ip"]

        self.dataframe = pd.concat(
            [
                pd.read_csv(file, sep="\s+", usecols=[0, 1, 2], names=self.headers)
                for file in self.files
            ]
        )

    def most_frequent_IP(self) -> source.ResponseIP:
        ip = self.dataframe["ip"].value_counts().index.tolist()[0]
        return source.ResponseIP(
            action=iplogs.MOST_FREQUENT_IP, files=self.files, ip=ip
        )

    def least_frequent_IP(self) -> source.ResponseIP:
        ip = self.dataframe["ip"].value_counts().index.tolist()[-1]
        return source.ResponseIP(
            action=iplogs.LEAST_FREQUENT_IP, files=self.files, ip=ip
        )

    def events_per_second(self) -> source.ResponseEvents:
        no_events = (
            self.dataframe["ip"].count()
            / self.dataframe["timestamp"].round(0).value_counts().count()
        )
        return source.ResponseEvents(
            action=iplogs.EVENTS_PER_SECOND, files=self.files, no_events=no_events
        )

    def total_amount_of_bytes_exchanged(self) -> source.ResponseBytes:
        no_bytes = self.dataframe["size"].sum()
        return source.ResponseBytes(
            action=iplogs.TOTAL_AMOUNT_OF_BYTES_EXCHANGED,
            files=self.files,
            no_bytes=no_bytes,
        )
