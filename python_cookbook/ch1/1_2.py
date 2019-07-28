# Unpacking Elements from Iterables of Arbitrary Length


def drop_first_last(grades):
    # Function for dropping the first and last element in the sequence
    first, *middle, last = grades
    print(type(middle))  # list

    print(middle)
    print(*middle)

    # star expression(*):
    # 1. When first declare it, it signifies that this would store all the unpacked
    # elements into a list;
    # 2. Later if you use the name without *, you get a list;
    # 3. If you use the name with prefix *, you get the unpacked values from the list.

    return middle


user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record
# It’s worth noting that the phone_numbers variable will always be a list, regardless of how
# many phone numbers are unpacked (including none).


drop_first_last(user_record)

*trailing, last = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(last)


# Function argumrn unpacking
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


# Example
line = 'nobody:*:-2:-2:Unprivileged_User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(fields)
print(homedir)
print(sh)


# Sometimes you might want to unpack values and throw them away.
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_1, (*_2, year) = record
print(_1)
print(_2)


# Recursive summing algorithm with star unpacking
nums = [1, 2, 3, 4, 5]
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print(sum(nums))