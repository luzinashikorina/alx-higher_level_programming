#!/usr/bin/python3


def no_c(my_string):

    inputList = list(my_string)
    resultString = ""
    counter = 0

    for i in range(0, len(inputList)):
        currentChar = inputList[counter]
        if currentChar != 'C' and currentChar != 'c':
            resultString = resultString + currentChar
        counter += 1

    return resultString
