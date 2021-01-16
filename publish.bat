copy /Y ..\GE_Pip.py "..\..\Box Sync\GE_Pip"
copy /Y ..\GE_Pip.py "..\..\OneDrive - Baker Hughes\Utility"
REM Published to Box and OneDrive - Publish to github.build.ge.com manually
explorer ..
explorer https://github.build.ge.com/GE-Pip-Maintainers/ge_pip/releases/new
