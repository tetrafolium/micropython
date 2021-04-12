try:
import uio
import uerrno
from frzqstr import returns_NULL
from frzmpy_pkg2.mod import Foo
from frzstr_pkg2.mod import Foo
import frzmpy_pkg1
import frzstr_pkg1
import frzmpy1
import frzstr1
import cppexample
import cexample
extra_coverage
except NameError:
    print("SKIP")
    raise SystemExit


data = extra_coverage()

# test hashing of str/bytes that have an invalid hash
print(data[0], data[1])
print(hash(data[0]))
print(hash(data[1]))
print(hash(bytes(data[0], "utf8")))
print(hash(str(data[1], "utf8")))

# test streams
stream = data[2]  # has set_error and set_buf. Write always returns error
stream.set_error(uerrno.EAGAIN)  # non-blocking error
print(stream.read())  # read all encounters non-blocking error
print(stream.read(1))  # read 1 byte encounters non-blocking error
print(stream.readline())  # readline encounters non-blocking error
print(stream.readinto(bytearray(10)))  # readinto encounters non-blocking error
print(stream.write(b"1"))  # write encounters non-blocking error
print(stream.write1(b"1"))  # write1 encounters non-blocking error
stream.set_buf(b"123")
print(stream.read(4))  # read encounters non-blocking error after successful reads
stream.set_buf(b"123")
# read1 encounters non-blocking error after successful reads
print(stream.read1(4))
stream.set_buf(b"123")
# readline encounters non-blocking error after successful reads
print(stream.readline(4))
try:
    # ioctl encounters non-blocking error; raises OSError
    print(stream.ioctl(0, 0))
except OSError:
    print("OSError")
stream.set_error(0)
print(stream.ioctl(0, bytearray(10)))  # successful ioctl call

stream2 = data[3]  # is textio
# read 1 byte encounters non-blocking error with textio stream
print(stream2.read(1))

# test BufferedWriter with stream errors
stream.set_error(uerrno.EAGAIN)
buf = uio.BufferedWriter(stream, 8)
print(buf.write(bytearray(16)))

# function defined in C++ code
print("cpp", extra_cpp_coverage())

# test user C module

print(cexample.add_ints(3, 2))

# test user C module mixed with C++ code

print(cppexample.cppfunc(1, 2))

# test basic import of frozen scripts

print(frzstr1.__file__)

print(frzmpy1.__file__)

# test import of frozen packages with __init__.py

print(frzstr_pkg1.__file__, frzstr_pkg1.x)

print(frzmpy_pkg1.__file__, frzmpy_pkg1.x)

# test import of frozen packages without __init__.py

print(Foo.x)

print(Foo.x)

# test raising exception in frozen script
try:
    import frzmpy2
except ZeroDivisionError:
    print("ZeroDivisionError")

# test loading a resource from a frozen string

buf = uio.resource_stream("frzstr_pkg2", "mod.py")
print(buf.read(21))

# test for MP_QSTR_NULL regression

print(returns_NULL())
