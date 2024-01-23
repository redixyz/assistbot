import os
import shutil
import zipfile
import getpass

source = ['config.py', 'localfuncs.py', 'markups.py']
dest = 'C://assistbot'

try:
    os.remove('config.py')
    shutil.rmtree(dest, ignore_errors=True)
except:
    pass

os.system('py cfggen.py')
os.system('python.exe -m pip install --upgrade pip')
os.system('pip install -r requirements.txt')

if not os.path.exists(dest):
    os.makedirs(dest)

for i in source:
    shutil.copy(f'{os.getcwd()}\\{i}', dest)

os.system('py nircmd.py')
