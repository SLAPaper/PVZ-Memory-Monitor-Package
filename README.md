# PVZ-Red-Eye-Monitor

Tool to Show the HP of Red-eyes in Plants vs. Zombies

## v0.0.3

### Screenshot

![screenshot](https://cloud.githubusercontent.com/assets/7543632/11874625/b3c9ee5a-a51b-11e5-84ef-87dd83855af8.png)

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
  - `ROW_GROUPS` is the way zombie list will be output, default is `((1,), (2,), (3,), (4,), (5,), (6,),)` (group by each row)
  - `REFRESH_TIME` is the period that the tool refresh the data, default is `1`(s)

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
  - `ROW_GROUPS` 是僵尸按行分组的方式，默认值为 `((1,), (2,), (3,), (4,), (5,), (6,),)` （每行都分别输出）
  - `REFRESH_TIME` 是工具刷新数据的周期，默认值为 `1`（秒）