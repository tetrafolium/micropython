from flashbdev import bdev
import uos
import gc

gc.threshold((gc.mem_free() + gc.mem_alloc()) // 4)

if bdev:
    try:
        uos.mount(bdev, "/")
    except:
        import inisetup

        inisetup.setup()

gc.collect()
