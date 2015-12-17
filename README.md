# PVZ-Red-Eye-Monitor
Tool to Show the HP of Red-eyes in Plants vs. Zombies

## v0.0.2
### English introduction
- Use Python 3.5.1
- Test on Python 3.5.1, Windows 10 Build 10586 (x64)
- Require pypiwin32 (Can be installed by running `pip install pypiwin32`)
- Search game by window title "Plants vs. Zombies", keep only one of them.
- Open game and enter Endless first 
- Only CLI
- Output sorted by `x` value of each zombie, group by 2, 5 row or 1, 6 row (Use on 两仪)
- Ctrl-C to exit

### 中文介绍
- 使用 Python 3.5.1 编写
- 在Windows 10 Build 10586 上测试通过
- 需要pypiwin32（命令行执行`pip install pypiwin32`来安装）
- 通过窗口标题"Plants vs. Zombies"来搜寻游戏，因此请关掉其它同名窗口（例如游戏文件夹）
- 先打开游戏并进入无尽模式再运行
- 只有命令行界面
- 红眼根据x轴坐标从小到大输出，根据岸路和边路分组（用于两仪）
- 按组合键Ctrl+C来退出