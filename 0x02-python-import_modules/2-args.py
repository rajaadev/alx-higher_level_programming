#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_args = len(sys.argv) - 1  # to exclude the script name
    if num_args == 0:
        print("0 argument")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} argument".format(num_args), end='')
    
    print("".format('' if num_args == 1 else 's'), end='')
    print("".format( ':' if num_args else '.'))

    if num_args > 0:
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))
