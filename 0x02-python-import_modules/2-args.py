#!/usr/bin/python3
import sys


def main():
    numberArgs = len(sys.argv) - 1

    print('{:d}'.format(numberArgs), end='')
    if numberArgs == 0:
        print(' arguments.')
    else:
        if numberArgs == 1:
            print(' argument:')
            print('{:d}: {:s}'.format(numberArgs, sys.argv[1]))
        else:
            print(' arguments:')
            for i in range(0, numberArgs):
                print('{:d}: {:s}'.format(i+1, sys.argv[i+1]))


if __name__ == "__main__":
    main()
