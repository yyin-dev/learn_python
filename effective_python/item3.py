""" str and bytes """

"""
There are two types that represent sequences of characters: bytes and str.
Instances of bytes contain raw 8-bit values(UTF-8). Instances of str 
contain Unicode characters. You can think of UTF-8 as way to encode character
as bits.

So: str -> bytes == Unicode --encode--> UTF-8
    bytes -> str == UTF-8 --decode--> Unicode

There are many ways to represent Unicode characters as binary data. The most 
common encoding is UTF-8. To convert Unicode characters to binary data, 
you must use the encode method. To convert binary data to Unicode characters, 
you must use the decode method.

Knowing would be enough.
"""

# You’ll need one method that takes a str or bytes and always returns a str.
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of str

# You’ll need another method that takes a str or bytes and always returns bytes.
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value # Instance of bytes

# In Python3, operations involving file handles (returned by the open built-in 
# function) default to UTF-8 encoding.









