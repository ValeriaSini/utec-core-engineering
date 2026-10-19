#!/usr/bin/env python3
def uppercase(str):
    result = ""
    for char in str:
        code = ord(char)
        code -= (ord("a") <= code <= ord("z")) * (ord("a") - ord("A"))
        result += chr(code)
    print(result)
