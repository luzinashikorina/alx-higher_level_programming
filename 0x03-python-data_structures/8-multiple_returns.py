#!/usr/bin/python3


def multiple_returns(sentence):

    inputLength = len(sentence)
    if inputLength > 0:
        return (inputLength, sentence[0])
    else:
        return (inputLength, None)
