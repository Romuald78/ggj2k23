rmdir dist /s /q
rmdir build /s /q
pyinstaller Launcher.py --collect-all arcade --onefile -w --add-data "resources;resources"