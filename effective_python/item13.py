import os
os.chdir("C:/Users/musicman/Desktop/learn_python/effective_python")

""" Take Advantage of Each Block in try/except/else/finally """


handle = open('random_data.txt', 'w', encoding='utf-8')
handle.write('success\nand\nnew\nlines')
handle.close()

""" 
Use try/finally when you want exceptions to propagate up, but you also want to 
run cleanup code even when exceptions occur. 
In the example below, any exception raised by read() will propogate to the 
calling code, yet close() is also guaranteed to run in finally block. 
Also note that, you must call open before the try block because exceptions that 
occur when opening the file (like IOError if the file does not exist) should 
skip the finally block, i.e., you should not call() close if enception is raised
during open.
"""
handle = open('random_data.txt')  # May raise IOError
try:
    data = handle.read()  # May raise UnicodeDecodeError
finally:
    handle.close()        # Always runs after try:


""" else block """
import json

def load_json_key(data, key):
    try:
        result_dict = json.loads(data)  # May raise ValueError
    except ValueError as e:
        raise KeyError from e
    else:
        return result_dict[key]         # May raise KeyError


""" try/except/else/finally all together """
import json
UNDEFINED = object()

def divide_json(path):
    handle = open(path, 'r+')   # May raise IOError
    try:
        data = handle.read()    # May raise UnicodeDecodeError
        op = json.loads(data)   # May raise ValueError
        value = (
            op['numerator'] /
            op['denominator'])  # May raise ZeroDivisionError
    except ZeroDivisionError as e:
        return UNDEFINED
    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)    # May raise IOError
        return value
    finally:
        handle.close()          # Always runs


