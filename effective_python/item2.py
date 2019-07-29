""" Style Guide """

"""
Whitespace:
Use space instead of tab.
Use 4 spaces for each indent level.
Lines should have less than 80 characters.
In a file, functions and classes should be separated by two blank lines.
In a class, methods should be separated by one blank line.
Don't put spaces around list indexes, function calls, or keyword argument 
assignments.
Put one—and only one—space before and after variable assignments.

Naming:
Functions, variables, and attributes should be in lowercase_underscore format.
Protected instance attributes should be in _leading_underscore format.
Private instance attributes should be in __double_leading_underscore format.
Classes and exceptions should be in CapitalizedWord format.
Module-level constants should be in ALL_CAPS format.

Expression and Statements:
Use inline negation (if a is not b) instead of negation of positive expressions
(if not a is b).
Don’t check for empty values (like [] or '') by checking the length (if
len(somelist) == 0). Use if not somelist and assume empty values
implicitly evaluate to False. The statement if somelist is implicitly True 
for non-empty values.
Avoid single-line if statements, for and while loops, and except compound
statements. Spread these over multiple lines for clarity.
Always put import statements at the top of a file.
Always use absolute names for modules when importing them, not names relative to
the current module’s own path. For example, to import the foo module from the
bar package, you should do from bar import foo, not just import foo.
If you must do relative imports, use the explicit syntax from . import foo.
Imports should be in sections in the following order: standard library modules, 
thirdparty modules, your own modules. Each subsection should have imports in
alphabetical order.

"""