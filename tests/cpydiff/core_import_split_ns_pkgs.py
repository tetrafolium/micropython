"""
categories: Core,import
description: MicroPython does't support namespace packages split across filesystem.
cause: MicroPython's import system is highly optimized for simplicity, minimal memory usage, and minimal filesystem search overhead.
workaround: Don't install modules belonging to the same namespace package in different directories. For MicroPython, it's recommended to have at most 3-component module search paths: for your current application, per-user (writable), system-wide (non-writable).
"""
import subpkg.bar
import subpkg.foo
import sys

sys.path.append(sys.path[1] + "/modules")
sys.path.append(sys.path[1] + "/modules2")


print("Two modules of a split namespace package imported")
