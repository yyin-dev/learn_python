import os
os.chdir("C:/Users/musicman/Desktop/learn_python/effective_python")

# Provide Optional Behavior with Keyword Arguments


def remainder(number, divisor):
    return number % divisor


# Following calls are equivalent.
# Positional arguments must be specified before keyword arguments.
remainder(20, 7)
remainder(20, divisor=7)
remainder(number=20, divisor=7)
remainder(divisor=7, number=20)


def flow_rate(weight_diff, time_diff):
    return weight_diff / time_diff

weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
print('%.3f kg per second' % flow)


def flow_rate(weight_diff, time_diff, period=1):
    return (weight_diff / time_diff) * period


flow_per_second = flow_rate(weight_diff, time_diff)
print('%.3f kg per second' % flow_per_second)
flow_per_hour = flow_rate(weight_diff, time_diff, period=3600)
print('%.3f kg per hour' % flow_per_hour)

# Benefits from keyword arguments:
# 1. Clarity and readability;
# 2. Provide default argument;
# 3. Provide a powerful way to extends a function's parameters while remaining
# backwards compatible with existing callers. 

def flow_rate(weight_diff, time_diff,
              period=1, units_per_kg=1):
    return ((weight_diff * units_per_kg) / time_diff) * period

pounds_per_hour = flow_rate(weight_diff, time_diff, period=3600, units_per_kg=2.2)
print('%.3f pound per hour' % pounds_per_hour)

# Supplying optional arguments(arguments with default value) positionally can 
# be confusing. The best practive is to always specify optional arugments using
# keyword names and never pass them as positional arguments.
