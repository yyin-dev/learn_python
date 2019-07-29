""" Write Helper Functions Instead of Complex Expressions """


from urllib.parse import parse_qs
my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
print(repr(my_values))
print(type(my_values))

# Value is not well formatted for empty or non-existent field.
print('Red:     ', my_values.get('red'))            # Value exists
print('Green:   ', my_values.get('green'))          # Value is blank
print('Opacity: ', my_values.get('opacity'))        # No such field

# Use default value to handle non-existent case
# Usage: dict.get(key[, default])
red = my_values.get('red', [''])
green = my_values.get('green', [''])
opacity = my_values.get('opacity', [''])
print('Red:     ', red)
print('Green:   ', green)
print('Opacity: ', opacity)

# Use or to handle empty value
red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0
print('Red:     ', red)
print('Green:   ', green)
print('Opacity: ', opacity)

# Convert to int, so that can be used in calculation
red = int(my_values.get('red', [''])[0] or 0)
green = int(my_values.get('green', [''])[0] or 0)
opacity = int(my_values.get('opacity', [''])[0] or 0)
print('Red:     ', red)
print('Green:   ', green)
print('Opacity: ', opacity)

# Improve readibility by spread the logic out in a helper function


def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found


red = get_first_int(my_values, 'red')
green = get_first_int(my_values, 'green')
opacity = get_first_int(my_values, 'opacity')
print('Red:     ', red)
print('Green:   ', green)
print('Opacity: ', opacity)
