# Example showing the use of the `sys` library

import sys

sys.stderr.write('this is stderr output stream\n') # stderr is unbuffered, should use for errors only
sys.stderr.flush() # flush buffer
sys.stdout.write('this is the stdout output stream\n\n') # should use for everything except errors

# sys `argv` command
print("\nsystem arguments (notice it returns a LIST):")
print(sys.argv) # all the arguments in a (0-based) LIST, remember the 1st argument is the file name

dsize = sys.getsizeof({}) # overhead of an empty dictionary
lsize = sys.getsizeof([]) # number bytes of an empty list
ssize = sys.getsizeof(set()) # num bytes of an empty set
print("\n-empty dictionary {} bytes\n-empty list {} bytes\n-empty set {} bytes\n".format(dsize, lsize, ssize))

'''
Output:
this is stderr output stream

this is the stdout output stream

system arguments (notice it returns a LIST):
['/opt/conda/lib/python3.5/site-packages/ipykernel/__main__.py', '-f', '/home/jovyan/.local/share/jupyter/runtime/kernel-24640232-2bba-487f-b37a-f3efec8c17b9.json']

-empty dictionary 288 bytes
-empty list 64 bytes
-empty set 224 bytes
'''
