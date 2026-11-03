#!/usr/bin/env python3

x = 10
print(f"x: {x}, Speicheradresse: {id(x)}")
x = x + 5
print(f"x: {x}, Speicheradresse: {id(x)}")
s = "Hallo"
print(f"s: {s}, Speicheradresse: {id(s)}")
s = s + " Welt"
print(f"s: {s}, Speicheradresse: {id(s)}")  
