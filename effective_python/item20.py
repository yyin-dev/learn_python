import os
os.chdir("C:/Users/musicman/Desktop/learn_python/effective_python")

# Use None and Docstrings to Specify Dynamic Default Arguments

from time import sleep
from datetime import datetime

def log(message, when=datetime.now()):
    # The timestamps would be the same because datetime.now() is only executed 
    # a single time: when the function is defined.
    # Default argument values are evaluated only ONCE per module load, which 
    # usually happens when a program starts up.
    # The convention for achieving the desired result in Python is to provide 
    # a default value of None and to document the behavior in the docstring.
    print('%s: %s' % (when, message))

log('Hi there!')
sleep(0.1)
log('Hi again!')


def log(message, when=None):
    """Log a message with a timestamp.
    Args:
        message: Message to print.
        when: datetime of when the message occurred.
            Defaults to the present time.
    """
    when = datetime.now() if when is None else when
    print('%s: %s' % (when, message))


log('Hi there!')
sleep(0.1)
log('Hi again!')


# Another example
import json

def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default


foo = decode('bad data')
foo['stuff'] = 5            # refer to the dict specified by default
bar = decode('also bad')
bar['meep'] = 1             # refer to the dict specified by default
print('Foo:', foo)
print('Bar:', bar)
assert foo is bar


def decode(data, default=None):
    """Load JSON data from a string.
    Args:
        data: JSON data to decode.
        default: Value to return if decoding fails.
            Defaults to an empty dictionary.
    """
    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default


foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)