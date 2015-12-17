import os, time, ctypes, win32ui, win32process, win32api
from win32file import GENERIC_READ

# reference: http://tieba.baidu.com/p/2843347257?fr=good
pvz = {
    "base": {
        "addr": 0x6A9EC0,
        "second": {
            "addr": 0x768,
            "zombies_count": {
                "addr": 0x94,
                "type": "int32",
            },
            "zombies": {
                "addr": 0x90,
                "step": 0x15C,
                "row": {
                    "addr": 0x1C,
                    "type": "int32",
                },
                "zombie_type": {
                    "addr": 0x24,
                    "type": "int32",
                },
                "x": {
                    "addr": 0x2C, 
                    "type": "float",
                },
                "y": {
                    "addr": 0x30,
                    "type": "float",
                },
                "is_fainted": {
                    "addr": 0xBA,
                    "type": "Byte",
                },
                "hp": {
                    "addr": 0xC8,
                    "type": "int32",
                },
                "hp_max": {
                    "addr": 0xCC,
                    "type": "int32",
                },
                "hp_equip1": {
                    "addr": 0xD0,
                    "type": "int32",
                },
                "hp_equip1_max": {
                    "addr": 0xD4,
                    "type": "int32",
                },
                "hp_equip2": {
                    "addr": 0xDC,
                    "type": "int32",
                },
                "hp_equip2_max": {
                    "addr": 0xE0,
                    "type": "int32",
                },
                "is_death": {
                    "addr": 0xEC,
                    "type": "Byte",
                },
                "is_hidden": {
                    "addr": 0x15A,
                    "type": "int16",
                },
            },
        },
    },
}

WINDOW_TITLE = "Plants vs. Zombies"
rPM = ctypes.windll.kernel32.ReadProcessMemory

def read_helper(handle, address, ctypes_var, n_bytes):
    if(rPM(handle, address, ctypes.byref(ctypes_var), n_bytes, None)):
        return ctypes_var.value
    else:
        raise MemoryError

def print_sorted_by_x(zombie_list):
    sorted_zombie_list = sorted(zombie_list, key=lambda item: item["x"])
    
    print("HP\trow\tx")
    for item in sorted_zombie_list:
        print("%d\t%d\t%.2f" % (item["hp"], item["row"], item["x"]))

window = win32ui.FindWindow(None, WINDOW_TITLE) 
hwnd = window.GetSafeHwnd()
pid = win32process.GetWindowThreadProcessId(hwnd)[1]
process = win32api.OpenProcess(GENERIC_READ, 0, pid)
handle = process.handle

base = read_helper(handle, pvz["base"]["addr"], ctypes.c_void_p(), 4)
second = read_helper(handle, base + pvz["base"]["second"]["addr"], ctypes.c_void_p(), 4)
zombies_count = read_helper(handle, second + pvz["base"]["second"]["zombies_count"]["addr"], ctypes.c_int32(), 4)

# search through the zombies list
zombies = pvz["base"]["second"]["zombies"]
first_zombie = read_helper(handle, second + zombies["addr"], ctypes.c_void_p(), 4)
step = zombies["step"]

try:
    while(True):
        zombies_list = []
        for p in range(first_zombie, first_zombie + zombies_count * step, step):
            is_death = read_helper(handle, p + zombies["is_death"]["addr"], ctypes.c_byte(), 1)
            
            if (not is_death):
                current_zombie = {}
                
                current_zombie["is_death"] = is_death
                current_zombie["hp"] = read_helper(handle, p + zombies["hp"]["addr"], ctypes.c_int32(), 4)
                current_zombie["row"] = read_helper(handle, p + zombies["row"]["addr"], ctypes.c_int32(), 4)
                current_zombie["zombie_type"] = read_helper(handle, p + zombies["zombie_type"]["addr"], ctypes.c_int32(), 4)
                current_zombie["x"] = read_helper(handle, p + zombies["x"]["addr"], ctypes.c_float(), 4)
                current_zombie["y"] = read_helper(handle, p + zombies["y"]["addr"], ctypes.c_float(), 4)
                current_zombie["hp_max"] = read_helper(handle, p + zombies["hp"]["addr"], ctypes.c_int32(), 4)
                current_zombie["hp_equip1"] = read_helper(handle, p + zombies["hp_equip1"]["addr"], ctypes.c_int32(), 4)
                current_zombie["hp_equip1_max"] = read_helper(handle, p + zombies["hp_equip1_max"]["addr"], ctypes.c_int32(), 4)
                current_zombie["hp_equip2"] = read_helper(handle, p + zombies["hp_equip2"]["addr"], ctypes.c_int32(), 4)
                current_zombie["hp_equip2_max"] = read_helper(handle, p + zombies["hp_equip2_max"]["addr"], ctypes.c_int32(), 4)
                current_zombie["is_hidden"] = read_helper(handle, p + zombies["is_hidden"]["addr"], ctypes.c_int16(), 2)
                
                zombies_list.append(current_zombie)
        
        red_list = [item for item in zombies_list if item["zombie_type"] == 32]
        
        os.system("cls")
        print_sorted_by_x(red_list)
        
        time.sleep(1)
except(KeyboardInterrupt):
    print("User exit")
    exit(0)