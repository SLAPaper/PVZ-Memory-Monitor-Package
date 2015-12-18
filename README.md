# PVZ-Red-Eye-Monitor

Tool to Show the HP of Red-eyes in Plants vs. Zombies

## v0.0.4

### Screenshot

![red_eye_monitor](https://cloud.githubusercontent.com/assets/7543632/11903096/b23efb12-a5f1-11e5-8a4d-fca1c3bbb103.png)

### English introduction

- Use Python 3.5.1
  - Python and pip installation tutorial, try [This (Chinese website)](http://www.tuicool.com/articles/eiM3Er3)
- Test on Python 3.5.1, Windows 10 Build 10586 (x64), Plants vs. Zombies 1.0.0.1051(en)
- Require pypiwin32 (Can be installed by running `pip install pypiwin32`)
- Search game by window title "Plants vs. Zombies", keep only one of them.
- Open game first, and then click `Run.bat`
- Only CLI
- Output sorted by `x` value of each zombie
- Press Ctrl-C to exit
- Config is at the top of `red_eye_monitor.py`
  - `WINDOW_TITLE` is the name of game Window, default is `"Plants vs. Zombies"`
  - `TRACK_TYPE` is the zombie type the tool will keep track of (refer to `ZOMBIE_NAME` below), default is `(32,)` (which is Red-eye)
  - `ROW_GROUPS` is the way zombie list will be output, default is `((1,), (2,), (3,), (4,), (5,), (6,),)` (group by each row)
  - `REFRESH_TIME` is the period that the tool refresh the data, default is `1`(s)
  - `REPLACE_X_WITH_COLUMN` is whether to use column to replace x, default is `True`
  - `SHOW_STATISTIC` is whether to show zombie statistics, deafult is `False`
  - `STATISTIC_ROW_GROUPS` is the way to group zombies, default is `ROW_GROUPS` (the same as `ROW_GROUPS`)
  - `STATISTIC_TRACK_TYPE` is the zombie type to count in statistic, by default is `(3, 8, 12, 14, 15, 17, 23, 32,)`

### 中文介绍

- 使用 Python 3.5.1 编写
  - Python 和 pip 的安装与配置，请参考 [这个链接](http://www.tuicool.com/articles/eiM3Er3)
- 在 Windows 10 Build 10586 上的 植物大战僵尸 1.0.0.1051 英文版 中测试通过
- 需要 pypiwin32（命令行执行 `pip install pypiwin32` 来安装）
- 通过窗口标题"Plants vs. Zombies"来搜寻游戏，因此请关掉其它同名窗口（例如游戏文件夹）
- 先打开游戏再运行 `Run.bat`
- 只有命令行界面
- 红眼根据x轴坐标从小到大输出
- 按组合键Ctrl+C来退出
- 用户设置在 `red_eye_monitor.py` 的顶部
  - `WINDOW_TITLE` 是游戏窗口的名字，默认值为 `"Plants vs. Zombies"`
  - `TRACK_TYPE` 是需要追踪的僵尸类型（参考下方的`ZOMBIE_NAME`），默认值为`(32,)`（红眼）
  - `ROW_GROUPS` 是僵尸按行分组的方式，默认值为 `((1,), (2,), (3,), (4,), (5,), (6,),)` （每行都分别输出）
  - `REFRESH_TIME` 是工具刷新数据的周期，默认值为 `1`（秒）
  - `REPLACE_X_WITH_COLUMN` 是是否用“列”来代替“x”坐标，默认值为 `True`
  - `SHOW_STATISTIC` 是是否显示僵尸统计，默认值是 `False`
  - `STATISTIC_ROW_GROUPS` 是僵尸统计中分组的方式，默认值为 `ROW_GROUPS` （即和`ROW_GROUPS`一致）
  - `STATISTIC_TRACK_TYPE` 是僵尸统计中需要计数的僵尸类型，默认值为 `(3, 8, 12, 14, 15, 17, 23, 32,)`