# below is User config
WINDOW_TITLE = "Plants vs. Zombies"
TRACK_TYPE = (32,)
ROW_GROUPS = ((1,), (2,), (3,), (4,), (5,), (6,),)
REFRESH_TIME = 1
REPLACE_X_WITH_COLUMN = True
SHOW_STATISTIC = False
STATISTIC_ROW_GROUPS = ROW_GROUPS
STATISTIC_TRACK_TYPE = (3, 8, 12, 14, 15, 17, 23, 32,)
# above is User config

import os, time, ctypes
from collections import OrderedDict

try:
    import win32ui, win32process, win32api
    from win32file import GENERIC_READ
except ImportError:
    print("The tool requires `pypiwin32` module, try `pip install pypiwin32` to install.")
    exit(1)

# reference: restricted material
ZOMBIE_NAME = {
    0: "普通",
    1: "旗帜",
    2: "路障",
    3: "撑杆",
    4: "铁桶",
    5: "报纸",
    6: "铁门",
    7: "橄榄",
    8: "跳舞",
    9: "伴舞",
    10: "游泳",
    11: "潜水",
    12: "冰车",
    13: "雪橇",
    14: "海豚",
    15: "小丑",
    16: "气球",
    17: "矿工",
    18: "跳跳",
    19: "雪人",
    20: "蹦极",
    21: "梯子",
    22: "投篮",
    23: "白眼",
    24: "小鬼",
    25: "Boss",
    26: "豌豆",
    27: "墙果",
    28: "辣椒",
    29: "机枪",
    30: "倭瓜",
    31: "高坚",
    32: "红眼",
}

# reference: http://tieba.baidu.com/p/2843347257?fr=good
PVZ = {
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
    }
}

rPM = ctypes.windll.kernel32.ReadProcessMemory

def calc_column_from_x(x):
    return (x - 40) / 80 + 1

def __read_helper(handle, address, ctypes_var, n_bytes):
    if(rPM(handle, address, ctypes.byref(ctypes_var), n_bytes, None)):
        return ctypes_var.value
    else:
        raise MemoryError

def __print_sort_by_x(zombie_list, group_by_row=None, replace_x_with_colunm=False):
    if group_by_row:
        zombie_group_by_row = OrderedDict()
        for row_group in group_by_row:
            zombie_group_by_row[tuple(row_group)] = []
        
        for zombie in zombie_list:
            for row_group in group_by_row:
                if zombie["row"] + 1 in row_group:
                     zombie_group_by_row[tuple(row_group)].append(zombie)
        
        for item in zombie_group_by_row.items():
            if len(item[1]) > 0:
                print("Row ", end="")
                for row_index in range(len(item[0])):
                    if row_index != 0:
                        print(", ", end="")
                    print(item[0][row_index], end="")
                
                sorted_zombie_list = sorted(item[1], key=lambda item: item["x"])
                if replace_x_with_colunm:
                    print("\nHP\tRow\tColumn\tType")
                    for zombie in sorted_zombie_list:
                        hp_total = zombie["hp"] + zombie["hp_equip1"] +zombie["hp_equip2"]
                        print("%d\t%d\t%.2f\t%s" % (hp_total, zombie["row"] + 1, calc_column_from_x(zombie["x"]), ZOMBIE_NAME[zombie["zombie_type"]]))
                else:
                    print("\nHP\tRow\tx\tType")
                    for zombie in sorted_zombie_list:
                        hp_total = zombie["hp"] + zombie["hp_equip1"] +zombie["hp_equip2"]
                        print("%d\t%d\t%.2f\t%s" % (hp_total, zombie["row"] + 1, zombie["x"], ZOMBIE_NAME[zombie["zombie_type"]]))
                
                print("")
    else:
        sorted_zombie_list = sorted(zombie_list, key=lambda item: item["x"])
        
        print("HP\tRow\tx")
        for zombie in sorted_zombie_list:
            print("%d\t%d\t%.2f" % (zombie["hp"], zombie["row"] + 1, zombie["x"]))

def __print_row_statistic(zombie_list, group_by_row=None):
    def __statistic_helper(zombie_list):
        zombie_statistic = {}
        for zombie in zombie_list:
            if zombie["zombie_type"] in zombie_statistic:
                zombie_statistic[zombie["zombie_type"]] += 1
            else:
                zombie_statistic[zombie["zombie_type"]] = 1
        return zombie_statistic
    
    print("Statistic")
    if group_by_row:
        zombie_group_by_row = OrderedDict()
        for row_group in group_by_row:
            zombie_group_by_row[tuple(row_group)] = []
        
        for zombie in zombie_list:
            for row_group in group_by_row:
                if zombie["row"] + 1 in row_group:
                        zombie_group_by_row[tuple(row_group)].append(zombie)
        
        is_first_row = True
        for item in zombie_group_by_row.items():
            if is_first_row:
                is_first_row = False
            else:
                print("")
            
            print("Row ", end="")
            for row_index in range(len(item[0])):
                if row_index != 0:
                    print(", ", end="")
                print(item[0][row_index], end="")
            print("", end="\t")
            
            zombie_statistic = __statistic_helper(item[1])
            sorted_zombie_statistic_list = sorted(list(zombie_statistic.items()), key=lambda item: item[0])
            for statistic_item in sorted_zombie_statistic_list:
                print("%s(%d)" % (ZOMBIE_NAME[statistic_item[0]], statistic_item[1]), end="\t")
    else:
        zombie_statistic = __statistic_helper(zombie_list)
        sorted_zombie_statistic_list = list(zombie_statistic.items()).sort(key=lambda item: item[0])
        for statistic_item in sorted_zombie_statistic_list:
            print("%s(%d)" % (ZOMBIE_NAME[statistic_item[0]], statistic_item[1]), end="\t")
    print("")


def main():
    window = win32ui.FindWindow(None, WINDOW_TITLE)
    hwnd = window.GetSafeHwnd()
    pid = win32process.GetWindowThreadProcessId(hwnd)[1]
    process = win32api.OpenProcess(GENERIC_READ, 0, pid)
    handle = process.handle
    
    try:
        while(True):
            try:
                base = __read_helper(handle, PVZ["base"]["addr"], ctypes.c_void_p(), 4)
                second = __read_helper(handle, base + PVZ["base"]["second"]["addr"], ctypes.c_void_p(), 4)
                zombies_count = __read_helper(handle, second + PVZ["base"]["second"]["zombies_count"]["addr"], ctypes.c_int32(), 4)
        
                # search through the zombies list
                zombies = PVZ["base"]["second"]["zombies"]
                
                first_zombie = __read_helper(handle, second + zombies["addr"], ctypes.c_void_p(), 4)
                step = zombies["step"]
                
                zombies_list = []
                for p in range(first_zombie, first_zombie + zombies_count * step, step):
                    is_death = __read_helper(handle, p + zombies["is_death"]["addr"], ctypes.c_byte(), 1)
                    
                    if (not is_death):
                        current_zombie = {}
                        
                        current_zombie["is_death"] = is_death
                        current_zombie["row"] = __read_helper(handle, p + zombies["row"]["addr"], ctypes.c_int32(), 4)
                        current_zombie["zombie_type"] = __read_helper(handle, p + zombies["zombie_type"]["addr"], ctypes.c_int32(), 4)
                        current_zombie["x"] = __read_helper(handle, p + zombies["x"]["addr"], ctypes.c_float(), 4)
                        current_zombie["y"] = __read_helper(handle, p + zombies["y"]["addr"], ctypes.c_float(), 4)
                        current_zombie["hp"] = __read_helper(handle, p + zombies["hp"]["addr"], ctypes.c_int32(), 4)
                        current_zombie["hp_max"] = __read_helper(handle, p + zombies["hp"]["addr"], ctypes.c_int32(), 4)
                        current_zombie["hp_equip1"] = __read_helper(handle, p + zombies["hp_equip1"]["addr"], ctypes.c_int32(), 4)
                        current_zombie["hp_equip1_max"] = __read_helper(handle, p + zombies["hp_equip1_max"]["addr"], ctypes.c_int32(), 4)
                        current_zombie["hp_equip2"] = __read_helper(handle, p + zombies["hp_equip2"]["addr"], ctypes.c_int32(), 4)
                        current_zombie["hp_equip2_max"] = __read_helper(handle, p + zombies["hp_equip2_max"]["addr"], ctypes.c_int32(), 4)
                        current_zombie["is_hidden"] = __read_helper(handle, p + zombies["is_hidden"]["addr"], ctypes.c_int16(), 2)
                        
                        zombies_list.append(current_zombie)
                
                track_list = (item for item in zombies_list if item["zombie_type"] in TRACK_TYPE)
                
                os.system("cls")
                __print_sort_by_x(track_list, group_by_row=ROW_GROUPS, replace_x_with_colunm=REPLACE_X_WITH_COLUMN)
                
                if SHOW_STATISTIC:
                    statistic_track_list = (item for item in zombies_list if item["zombie_type"] in STATISTIC_TRACK_TYPE)
                    __print_row_statistic(statistic_track_list, group_by_row=STATISTIC_ROW_GROUPS)
                
            except TypeError:
                pass
            
            time.sleep(REFRESH_TIME)
    except(KeyboardInterrupt):
        print("User exit")
        exit(0)

if __name__ == "__main__":
    main()