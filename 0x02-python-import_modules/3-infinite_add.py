#!/usr/bin/python3
import sys


def main():

    numberArguments = len(sys.argv) - 1
    counter = 0

    if numberArguments > 0:
        for i in range(0, numberArguments):
            counter = counter + int(sys.argv[i+1])
        print(counter)
    else:
        print('0')


if __name__ == '__main__':
    main()
