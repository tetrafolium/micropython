# test large function (stack) state

# this function creates 127 locals
def f():
    x0 = 1
    x1 = 1
    x2 = 1
    x3 = 1
    x4 = 1
    x5 = 1
    x6 = 1
    x7 = 1
    x8 = 1
    x9 = 1
    x10 = 1
    x11 = 1
    x12 = 1
    x13 = 1
    x14 = 1
    x15 = 1
    x16 = 1
    x17 = 1
    x18 = 1
    x19 = 1
    x20 = 1
    x21 = 1
    x22 = 1
    x23 = 1
    x24 = 1
    x25 = 1
    x26 = 1
    x27 = 1
    x28 = 1
    x29 = 1
    x30 = 1
    x31 = 1
    x32 = 1
    x33 = 1
    x34 = 1
    x35 = 1
    x36 = 1
    x37 = 1
    x38 = 1
    x39 = 1
    x40 = 1
    x41 = 1
    x42 = 1
    x43 = 1
    x44 = 1
    x45 = 1
    x46 = 1
    x47 = 1
    x48 = 1
    x49 = 1
    x50 = 1
    x51 = 1
    x52 = 1
    x53 = 1
    x54 = 1
    x55 = 1
    x56 = 1
    x57 = 1
    x58 = 1
    x59 = 1
    x60 = 1
    x61 = 1
    x62 = 1
    x63 = 1
    x64 = 1
    x65 = 1
    x66 = 1
    x67 = 1
    x68 = 1
    x69 = 1
    x70 = 1
    x71 = 1
    x72 = 1
    x73 = 1
    x74 = 1
    x75 = 1
    x76 = 1
    x77 = 1
    x78 = 1
    x79 = 1
    x80 = 1
    x81 = 1
    x82 = 1
    x83 = 1
    x84 = 1
    x85 = 1
    x86 = 1
    x87 = 1
    x88 = 1
    x89 = 1
    x90 = 1
    x91 = 1
    x92 = 1
    x93 = 1
    x94 = 1
    x95 = 1
    x96 = 1
    x97 = 1
    x98 = 1
    x99 = 1
    x100 = 1
    x101 = 1
    x102 = 1
    x103 = 1
    x104 = 1
    x105 = 1
    x106 = 1
    x107 = 1
    x108 = 1
    x109 = 1
    x110 = 1
    x111 = 1
    x112 = 1
    x113 = 1
    x114 = 1
    x115 = 1
    x116 = 1
    x117 = 1
    x118 = 1
    x119 = 1
    x120 = 1
    x121 = 1
    x122 = 1
    x123 = 1
    x124 = 1
    x125 = 1
    x126 = 1


f()

# this function pushes 128 elements onto the function stack


def g():
    x = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ]


g()

# this function exercises load_fast_n and store_fast_n opcodes


def h():
    x0 = 1
    x1 = x0
    x2 = x1
    x3 = x2
    x4 = x3
    x5 = x4
    x6 = x5
    x7 = x6
    x8 = x7
    x9 = x8
    x10 = x9
    x11 = x10
    x12 = x11
    x13 = x12
    x14 = x13
    x15 = x14
    x16 = x15
    x17 = x16


h()
