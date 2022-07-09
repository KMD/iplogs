import pandas as pd
from sources import squid

def test_answer():
    assert True

def test_init_file():
    factory = squid.Squid(["tests/test_logs/access1.log"])
    assert factory.files == ["tests/test_logs/access1.log"]
    assert type(factory.dataframe) == pd.core.frame.DataFrame
    assert factory.most_frequent_IP().json() == '{"action": "MostFrequentIP", "files": ["tests/test_logs/access1.log"], "ip": "127.0.0.1"}'
    assert factory.least_frequent_IP().json() == '{"action": "LeastFrequentIP", "files": ["tests/test_logs/access1.log"], "ip": "219.103.55.23"}'

