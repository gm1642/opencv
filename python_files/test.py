import sys
print(len(sys.argv))
print(sys.argv[0])#by default displays the file name
print(sys.argv[1])#this line is used only when we need to recieve the argument

# Windows PowerShell
# Copyright (C) Microsoft Corporation. All rights reserved.

# Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

# Warning: PowerShell detected that you might be using a screen reader and has disabled PSReadLine for compatibility purposes. If you want to re-enable it, run 'Import-Module PSReadLine'.

# PS C:\Windows\system32> cd C:\Users\samkh\Documents\python\opencv
# PS C:\Users\samkh\Documents\python\opencv> .\env1\Scripts\activate
# .\env1\Scripts\activate : File C:\Users\samkh\Documents\python\opencv\env1\Scripts\activate.ps1 cannot be loaded
# because running scripts is disabled on this system. For more information, see about_Execution_Policies at
# https:/go.microsoft.com/fwlink/?LinkID=135170.
# At line:1 char:1
# + .\env1\Scripts\activate
# + ~~~~~~~~~~~~~~~~~~~~~~~
#     + CategoryInfo          : SecurityError: (:) [], PSSecurityException
#     + FullyQualifiedErrorId : UnauthorizedAccess
# PS C:\Users\samkh\Documents\python\opencv> set-executionpolicy remotesigned

# Execution Policy Change
# The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose
# you to the security risks described in the about_Execution_Policies help topic at
# https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to change the execution policy?
# [Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): Y
# PS C:\Users\samkh\Documents\python\opencv> set-executionpolicy remotesigned

# Execution Policy Change
# The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose
# you to the security risks described in the about_Execution_Policies help topic at
# https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to change the execution policy?
# [Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): y
# PS C:\Users\samkh\Documents\python\opencv> virtualenv
# usage: virtualenv [--version] [--with-traceback] [-v | -q] [--read-only-app-data] [--app-data APP_DATA] [--reset-app-data] [--upgrade-embed-wheels] [--discovery {builtin}] [-p py] [--try-first-with py_exe]
#                   [--creator {builtin,cpython3-win,venv}] [--seeder {app-data,pip}] [--no-seed] [--activators comma_sep_list] [--clear] [--no-vcs-ignore] [--system-site-packages] [--symlinks | --copies] [--no-download | --download]
#                   [--extra-search-dir d [d ...]] [--pip version] [--setuptools version] [--wheel version] [--no-pip] [--no-setuptools] [--no-wheel] [--no-periodic-update] [--symlink-app-data] [--prompt prompt] [-h]
#                   dest
# virtualenv: error: the following arguments are required: dest
# SystemExit: 2
# PS C:\Users\samkh\Documents\python\opencv> virtualenv
# usage: virtualenv [--version] [--with-traceback] [-v | -q] [--read-only-app-data] [--app-data APP_DATA] [--reset-app-data] [--upgrade-embed-wheels] [--discovery {builtin}] [-p py] [--try-first-with py_exe]
#                   [--creator {builtin,cpython3-win,venv}] [--seeder {app-data,pip}] [--no-seed] [--activators comma_sep_list] [--clear] [--no-vcs-ignore] [--system-site-packages] [--symlinks | --copies] [--no-download | --download]
#                   [--extra-search-dir d [d ...]] [--pip version] [--setuptools version] [--wheel version] [--no-pip] [--no-setuptools] [--no-wheel] [--no-periodic-update] [--symlink-app-data] [--prompt prompt] [-h]
#                   dest
# virtualenv: error: the following arguments are required: dest
# SystemExit: 2
# PS C:\Users\samkh\Documents\python\opencv> pip install virtualenv
# Requirement already satisfied: virtualenv in c:\users\samkh\appdata\local\programs\python\python311\lib\site-packages (20.24.2)
# Requirement already satisfied: distlib<1,>=0.3.7 in c:\users\samkh\appdata\local\programs\python\python311\lib\site-packages (from virtualenv) (0.3.7)
# Requirement already satisfied: filelock<4,>=3.12.2 in c:\users\samkh\appdata\local\programs\python\python311\lib\site-packages (from virtualenv) (3.12.2)
# Requirement already satisfied: platformdirs<4,>=3.9.1 in c:\users\samkh\appdata\local\programs\python\python311\lib\site-packages (from virtualenv) (3.9.1)
# PS C:\Users\samkh\Documents\python\opencv> virtualenv env1
# created virtual environment CPython3.11.4.final.0-64 in 637ms
#   creator CPython3Windows(dest=C:\Users\samkh\Documents\python\opencv\env1, clear=False, no_vcs_ignore=False, global=False)
#   seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\samkh\AppData\Local\pypa\virtualenv)
#     added seed packages: pip==23.2.1, setuptools==68.0.0, wheel==0.41.0
#   activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
# PS C:\Users\samkh\Documents\python\opencv> .\env1\Scripts\activate
# (env1) PS C:\Users\samkh\Documents\python\opencv> pip freeze>requirement.txt
# ERROR: unknown command "freeze>requirement.txt"
# (env1) PS C:\Users\samkh\Documents\python\opencv> pip freeze>requirement.txt
# ERROR: unknown command "freeze>requirement.txt"
# (env1) PS C:\Users\samkh\Documents\python\opencv> pip freeze > requirement.txt
# (env1) PS C:\Users\samkh\Documents\python\opencv> pip install -r .\requirement.txt
# (env1) PS C:\Users\samkh\Documents\python\opencv> virtualenv --system-site-packages env2
# created virtual environment CPython3.11.4.final.0-64 in 660ms
#   creator CPython3Windows(dest=C:\Users\samkh\Documents\python\opencv\env2, clear=False, no_vcs_ignore=False, global=True)
#   seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\samkh\AppData\Local\pypa\virtualenv)
#     added seed packages: pip==23.2.1, setuptools==68.0.0, wheel==0.41.0
#   activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
# (env1) PS C:\Users\samkh\Documents\python\opencv> .\env2\Scripts\activate
# (env2) PS C:\Users\samkh\Documents\python\opencv> cd python_files
# (env2) PS C:\Users\samkh\Documents\python\opencv\python_files> python test.py
# (env2) PS C:\Users\samkh\Documents\python\opencv\python_files> python test.py
# 1
# test.py
# (env2) PS C:\Users\samkh\Documents\python\opencv\python_files> python test.py umar_khan
# 2
# test.py
# umar_khan
# (env2) PS C:\Users\samkh\Documents\python\opencv\python_files>

