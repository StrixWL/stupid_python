import sys as sys

def whatis(args):
    if len(args) == 0:
        exit(0)
    elif len(args) > 2:
        print(AssertionError("AssertionError: more than one argument is provided"))
        exit(1)
    arg = sys.argv[1]
    try:
        int(arg)
    except:
        print(AssertionError("AssertionError: argument is not an integer"))
        exit(1)
    arg = arg.strip()
    if arg[-1] in ["0", "2", "4", "6", "8"]:
        print("I'm Even.")
    else:
        print("I'm Odd.")

whatis(sys.argv)