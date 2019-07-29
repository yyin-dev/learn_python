import os
os.chdir("C:/Users/musicman/Desktop/learn_python/effective_python")

""" Prefer enumerate Over range(len()) """

""" basic iteration """
flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for flavor in flavor_list:
    print('%s is delicious' % flavor)


""" iterate with knowing index with range() """
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print('%d: %s' % (i + 1, flavor))


""" enumerate() is preferred """ 
for i, flavor in enumerate(flavor_list):
    print('%d: %s' % (i + 1, flavor))
