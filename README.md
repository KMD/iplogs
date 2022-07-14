# iplogs
- there is no log files attached into project (github allow only files smaller than 50MB), so if you want to test it you should attach example file. (You can name it *access1.log* and *access2.log* and put it into *tests/test_logs* folder)
- There is only support for one type of log files (example one)
## Usage

```git clone git@github.com:KMD/iplogs.git```

```cd iplogs```

```python3 -m venv env```

```source env/bin/activate```

```pip install -r requirements.txt```

Now you can use `iplogs` command. See Tutorial below.

## Usage with docker
```git clone git@github.com:KMD/iplogs.git```

```cd iplogs```

```docker build -t iplogs --rm . ```

```sudo docker run -it --name my_app --rm iplogs```

Now you can use `iplogs` command. See Tutorial below.

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

## Save to file

```python iplogs.py --action=MostFrequentIP --files="tests/test_logs" > result.json```