import os
os.chdir("C:/Users/musicman/Desktop/python_learning/python_crash_course")

# Writing to File
output_file = "output.txt"
with open(output_file, 'w') as file_object:
    # Modes available:
    # 'r': read;
    # 'w': (over)write;
    # 'a': append.
    # 'r+': raed and write.
    # default: 'r'.
    file_object.write("I love programming.")