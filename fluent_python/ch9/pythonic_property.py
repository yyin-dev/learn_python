# https://www.programiz.com/python-programming/property
# Unlike object attributes define with self.attr_name, property defined with
# @property decorator is not stored in __dict__ of the attribute. Instead, 
# the getter is called when the attribute is accessed, and the setter(if any), 
# is called when the user tries to set the attribute. If the setter is not
# defined, trying to set it raises an AttributeError.