import usys
import micropython

# unsigned ints


@micropython.viper
def viper_uint() -> uint:
    return uint(-1)


print(viper_uint() == (usys.maxsize << 1 | 1))
