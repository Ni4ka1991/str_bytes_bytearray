#! /usr/bin/env python3

from os import system
import sys


system("clear")
print( f"sys.getdefaultencoding() >>> {sys.getdefaultencoding()}" )
print()
print(f'ord("r") >>> { ord("r")} ' )
print(f'chr(208) >>> { chr(208)} ' )
print()
s = 'Python'
print( f"s = 'Python'" )

enc_ascii = s.encode('ascii')
enc_utf8 = s.encode('utf-8')
enc_utf16 = s.encode('utf-16')
print()
print(f"type(s.encode('ascii')) >>> {type( enc_ascii )}" )
print()

print(f"enc_ascii >>> {enc_ascii}" )
print(f"enc_utf8  >>> {enc_utf8 }" )
print(f"enc_utf16 >>> {enc_utf16}" )
print()

print(f"len(enc_ascii) >>> {len(enc_ascii)}" )
print(f"len(enc_utf8)  >>> {len(enc_utf8)}" )
print(f"len(enc_utf16) >>> {len(enc_utf16)}" )

