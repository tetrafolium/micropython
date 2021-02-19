"""
categories: Types,int
description: No int conversion for int-derived types available
cause: Unknown
workaround: Avoid subclassing builtin types unless really needed. Prefer https://en.wikipedia.org/wiki/Composition_over_inheritance .
"""


class A(int):
    def __add__(self, other):
        return A(int(self) + other)


a = A(42)
print(a + a)
