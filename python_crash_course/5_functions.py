# Positional argument: order matters
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".\n")


describe_pet('harry', 'hamster')
describe_pet('hamster', 'harry')

# Keyword argument: order does not matter
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# Modifying a List in a Function
# When you pass a list to a function, the function can modify the list. Any
# changes made to the list inside the function’s body are permanent, to
# avoid copying.
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Preventing a Function from Modifying a List
# You can send a copy of a list to the function. function_name(list_name[:])

# Passing an Arbitrary Number of Arguments, star unpacking
def print_arbritrary_num_args(*args):
    """
    The asterisk in the parameter name *toppings tells Python to make an
    empty tuple called args, and pack whatever values it receives into this
    tuple.
    Note that Python packs the arguments into a tuple, even if 
    the function receives only one value.
    """
    print(args)

print_arbritrary_num_args('the only arg')
print_arbritrary_num_args('mushrooms', 'green peppers', 'extra cheese')

# Mixing Positional and Arbitrary Arguments
def mix(required, *optional):
    print("Required arg: {}".format(required))
    print("Optional arg(s): {}".format(optional))
    # print(type(optional))
    # print(*optional)
    # print(type(*optional)) # Causes error

mix('the only arg')
mix('mushrooms', 'green peppers', 'extra cheese')

# Using Arbitrary Keyword Arguments
def build_profile(first, last, **user_info):
    """
    The double asterisks before the parameter **user_info cause Python to 
    create an empty dictionary called user_info and pack whatever name-value 
    pairs it receives into this dictionary.
    """
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    # Add pairs in user_info into profile
    for key, value in user_info.items():
        profile[key] = value
        return profile
        
user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')
print(user_profile)

"""
Styling Functions.

Functions should have descriptive names, and these names should use
lowercase letters and underscores.

Every function should have a comment that explains concisely what
the function does. This comment should appear immediately after the
function definition and use the docstring format.

If you specify a default value for a parameter, no spaces should be used
on either side of the equal sign:
    def function_name(parameter_0, parameter_1='default value')
The same convention should be used for keyword arguments in function calls: 
    function_name(value_0, parameter_1='value')

If a set of parameters causes a function’s definition to
be longer than 79 characters, press ENTER after the opening parenthesis on
the definition line. On the next line, press TAB twice to separate the list of
arguments from the body of the function, which will only be indented one
level.
        def function_name(
                parameter_0, parameter_1, parameter_2,
                parameter_3, parameter_4, parameter_5):
            function body...
"""
