import ctypes
import typing as tg

try:
    import win32ui
    import win32process
    import win32api
    from win32file import GENERIC_READ
except ImportError:
    print("The tool requires `pypiwin32` module, try `pip install pypiwin32` to install.")
    exit(1)

rPM = ctypes.windll.kernel32.ReadProcessMemory


def read_helper(handle, address, ctypes_var, n_bytes: int) -> bytes:
    if (rPM(handle, address, ctypes.byref(ctypes_var), n_bytes, None)):
        return ctypes_var.value
    else:
        raise MemoryError
