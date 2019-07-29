import os
os.chdir("C:/Users/musicman/Desktop/learn_python/effective_python")

for i in range(17, 60):
    with open("item{}.py".format(str(i)), 'w') as f:
        f.write('import os\n')
        f.write('os.chdir("C:/Users/musicman/Desktop/learn_python/'
                + 'effective_python")\n\n')
        f.write('#\n')
