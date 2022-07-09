# iplogs
## Usage
## Usage with docker
## Tutorial

Getting help with arguments:

```python iplogs.py --help```

Example usage for one file:

```python iplogs.py --action=MostFrequentIP --files="tests/test_logs/access1.log"```

Example usage for many files:

```python iplogs.py --action=MostFrequentIP --files="tests/test_logs/access1.log;tests/test_logs/access2.log"```

Example usage for directory:

```python iplogs.py --action=MostFrequentIP --files="tests/test_logs"```

Allowed actions:

```
MostFrequentIP
LeastFrequentIP
EventsPerSecond
TotalAmountOfBytesExchanged
```

Types:

```python iplogs.py --type="squid" --action=MostFrequentIP --files="tests/test_logs"```

There is support just for one log type: `squid` and is set to default.
