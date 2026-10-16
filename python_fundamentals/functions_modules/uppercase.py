#!/usr/bin/env python3
def uppercase(str):
    result = ""
    for char in str if isinstance(str, str) else chr(str):
        code = ord(char)
        if ord("a") <= code <= ord("z"):
            code -= ord("a") - ord("A")
        result += chr(code)
    print(result)
