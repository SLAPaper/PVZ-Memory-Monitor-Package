# PVZ-Red-Eye-Monitor
Tool to Show the HP of Red-eyes in Plants vs. Zombies

## v0.0.1
- Use Python 3.5.1
- Test on Python 3.5.1, Windows 10 Build 10586 (x64)
- Require pypiwin32 (Can be installed by running `pip install pypiwin32`)
- Search game by window title "Plants vs. Zombies", keep only one of them.
- Only CLI
- Output sorted by `x` value of each zombie
- Ctrl-C to exit

- 使用 Python 3.5.1 编写
- 在Windows 10 Build 10586 上测试通过
- 需要pypiwin32（命令行执行`pip install pypiwin32`来安装）
- 通过窗口标题"Plants vs. Zombies"来搜寻游戏，因此请关掉其它同名窗口（例如游戏文件夹）
- 只有命令行界面
- 红眼根据x轴坐标从小到大输出
- 按组合键Ctrl+C来退出