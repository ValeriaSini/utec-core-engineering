#!/usr/bin/env python3
def uppercase(str):
    result = ""
    for char in str:
        code = ord(char)
        if code >= 97 and code <= 122:
            code -= 32
        result += chr(code)
    print(result)
