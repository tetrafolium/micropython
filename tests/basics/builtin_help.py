# test builtin help function

try:
import micropython
help
except NameError:
    print("SKIP")
    raise SystemExit

help()  # no args
help(help)  # help for a function
help(int)  # help for a class
help(1)  # help for an instance
help(micropython)  # help for a module
help('modules')  # list available modules

print('done')  # so last bit of output is predictable
