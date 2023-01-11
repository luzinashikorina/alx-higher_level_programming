#!/usr/bin/python3
import hidden_4


def main():
    for n in dir(hidden_4):
        if n[1] != "_":
            print(n)


if __name__ == '__main__':
    main()
