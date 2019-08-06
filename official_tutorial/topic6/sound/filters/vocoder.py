import sys
import os
print(os.getcwd())
print(sys.path[:2])


# Run with:
# cd topic6/
# python -m sound.filters.vocoder
# Absolute import
import sound.effects.echo
from sound.effects import reverse
reverse.reverse()
# Relative import
from .. import test
test.test()
from ..formats import wav
wav.wav()


# Run with:
# cd sound/
# python -m filters.vocoder
# import effects.echo

print("Successful import!")

# Python interpreter does not know the working directory where the command line
# is started. For example, when running "python foo/bar/test.py", "foo/" is not
# added to sys.path, but "bar/", containing the running script, is added to
# sys.path. 

# Use -m flag to run the script as a module
# python -m package.subpackage.module or python -m package.module

# When you at at sound/ directory. Running "python filters/vocoder.py"
# would add "sound/filters/" to sys.path. However, if you run 
# "python -m filters.vocoder", "sound/"(current directory) would be 
# added to sys.path. -m flag adds current directory and is more intuitive.
# Thus, should try to use -m flag whenver possible to make absolute import
# works as expected.