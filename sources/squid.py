from typing import List

from sources import source


class Squid(source.Source):
    def __init__(files: List[str]):
        pass

    def most_frequent_IP(self) -> source.ResponseIP:
        return source.ResponseIP(action="aaa", files=["bbb", "vvv"], ip="127.0.0.1")

    def least_frequent_IP(self) -> source.ResponseIP:
        pass

    def events_per_second(self) -> source.ResponseEvents:
        pass

    def total_amount_of_bytes_exchanged(self) -> source.ResponseBytes:
        pass
