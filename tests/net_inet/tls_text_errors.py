# test that modtls produces a text error message

try:
    import usocket as socket
    import ussl as ssl
    import sys
except:
    import socket
    import ssl
    import sys


def test(addr):
    s = socket.socket()
    s.connect(addr)
    try:
        s = ssl.wrap_socket(s)
        print("wrap: no exception")
    except OSError as e:
        # mbedtls produces "mbedtls -0x7200: SSL - An invalid SSL record was received"
        # axtls produces "RECORD_OVERFLOW" but also prints "TLS buffer overflow,..."
        # CPython produces "[SSL: WRONG_VERSION_NUMBER] wrong version number (_ssl.c:1108)"
        ok = (
            "SSL_INVALID_RECORD" in str(e)
            or "RECORD_OVERFLOW" in str(e)
            or "wrong version" in str(e)
        )
        print("wrap:", ok)
        if not ok:
            print("got exception:", e)
    s.close()


if __name__ == "__main__":
    # connect to plain HTTP port, oops!
    addr = socket.getaddrinfo("micropython.org", 80)[0][-1]
    test(addr)
