# Module
# A module is a file containing Python definitions and statements. The file
# name is the module name with the suffix .py appended. Within a module, the 
# module's name is available as the value of the global variable __name__.

print(__name__)

import fibo
fibo.fib(500)
print(fibo.fib2(500))
print(fibo.__name__)
fib = fibo.fib
fib2 = fibo.fib2


# More on modules
# A module can contains executable statements as well as function defintions.
# These statements are intended to initialize the module. They are executed
# only the first time the module name is encountered in an import statement. 
#
# Each module has its own private symbol table, which is used as the global
# symbol table by all functions defined in the module. Thus, the author of the
# module can use global variables without worrying out naming conflict with the
# user of the module. In addition, you can access a module's global variables
# with the same notations as accessing functions: module_name.item_name. 
#
# The names of imported module are placed in the importing module's global 
# symbol table.

# Different importing statements.
from fibo import fib, fib2
from fibo import *
import fibo as fib
from fibo import fib as fibonacci, fib2 as fibonacci2


# The module search path
# When a module named spam is imported, the interpreter first searches for a 
# built-in module with that name. If not found, it then searches for a file
# named spam.py in the list of directories listed in the variable sys.path. 
# The variable sys.path is initialized from these locations:
# - The directories containering the input script;
# - PYTHONPATH;
# - THe installation-dependent default;
# Note that the directory containing the script being run is searched before
# the standard library. The sequence is: built-in modules -> modules sys.path
#  -> modules in standard library.
# 
# To speed up module loading, Python caches the compiled version of each module
# in the __pycache__ directory under the name: module_name.version.pyc, like:
# fibo.cpython-36.pyc.
# A program doesn't run any faster when it is loaded from a .pyc file or .py
# file. The only difference is the loading speed.


# The built-in function dir() is used to find out which names a module define.
# It returns a sorted list of strings.
import fibo, sys
print(dir(fib))
print(dir(sys))

# Without argument, dir() list the names you defined currently, including
# variables, modules, functions, etc.
print(dir())


# Package
# Packages are a way to structuring Python module namespace by using "dotted
# module names". Just like the use of module saves the authors of different 
# modules from having to worry about each other's global variable name, the use
# of dotted module names saves the authors or multimodule package from having
# to worry about each other's module name. That is, modules in different 
# packages can have the same name.
# The __init__.py is required to make Python treat directories containing the
# file as packages. This avoids directories with a common name, like "string",
# unintentionally hiding valid modules that occur later on the module search
# path. __init__.py can just be an empty file, but it can also execute 
# initialization code for the package or set the __all__ variable.
# 
# sound/                          Top-level package
#       __init__.py               Initialize the sound package
#       formats/                  Subpackage for file format conversions
#               __init__.py
#               wavread.py
#               wavwrite.py
#               aiffread.py
#               aiffwrite.py
#               auread.py
#               auwrite.py
#               ...
#       effects/                  Subpackage for sound effects
#               __init__.py
#               echo.py
#               surround.py
#               reverse.py
#               ...
#       filters/                  Subpackage for filters
#               __init__.py
#               equalizer.py
#               vocoder.py
#               karaoke.py
#               ...

# - import module directly
# import sound.effects.echo
# sound.effects.echo.echofilter(input)

# - from package import module
# from sound.effects import echo
# echo.echofilter(input)

# - from module import function
# from sound.effects.echo import echofilter
# echofilter(input)

# from sound.effects import *
# The above statement does not import all modules in the sound.effects package.
# The reason is that this could be very slow and result in unwanted sideeffects.
#
# The only solution is for the package author to provide an explicit index of
# the package. The import statement follows this convention: if the package's
# __init__.py defines a list named __all__, it is taken to be the list of
# module names that should be imported when from package import * is seen. It
# is up to the author to keep this list up-to-date. If you omit defining
# __all__ in the __init__.py of the package, from package import * would not
# import any module defined in the packge. It only imports the package and
# any names defined in the package. This includes any names defined by 
# __init__.py, as well as any submodules of the package that were explicitly
# loaded by previous import statements.
# https://stackoverflow.com/a/16595377/9057530
#


# Python import
# 
# When packages are structured into subpackages, you can use absolute imports
# to refer to submodules of sibling packages. For module sound.filters.vocoder,
# it can use from sound.effects import echo. Check sound/filters/vocoder.py
#
# You can also write relative imports, with "from module import name" form. 
# Note that in relative import, module must be prefixed with "."(including "..")
# Any import form not started with "." is considered aboslute import. 
# Absolute import is preferred over relative import. Any script using relative
# import cannot be run directly!!! "Note that relative imports are based on the
# name of the current module. Since the name of the main module is always 
# “main”, modules intended for use as the main module of a Python application 
# must always use absolute imports."
# https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
# When writing import statments, you need to consider whether the script
# would be run directly, and whether it would be imported as a module.
# 
# Seems that changing sys.path is a dirty solution but is quick and works well. 
# I will use this until a much better solution is available.