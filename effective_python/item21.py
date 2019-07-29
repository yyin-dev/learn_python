import os
os.chdir("C:/Users/musicman/Desktop/learn_python/effective_python")

# Enforce Clarity with Keyword-Only Arguments


def safe_division(number, divisor, ignore_overflow,
                  ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


result = safe_division(1.0, 10**500, True, False)
print(result)
assert result is 0

result = safe_division(1.0, 0, False, True)
print(result)
assert result == float('inf')


# Improve readability by setting default to False
def safe_division_b(number, divisor,
                    ignore_overflow=False,
                    ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


# But you can still call it with:
safe_division_b(1.0, 10**500, True, False)


# You can demand clarity by defining your functions with keyword-only
# arguments. These arguments can only be supplied by keyword, not by position.
# The * symbol in the argument list indicates the end of positional arguments 
# and the beginning of keyword-only arguments.


def safe_division_c(number, divisor, *,
                    ignore_overflow=False,
                    ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


safe_division_c(1.0, 0, ignore_zero_division=True)  # No exception
try:
    safe_division_c(1.0, 0)
    assert False
except ZeroDivisionError as e:
    print("Expected.")
    pass  # Expected
