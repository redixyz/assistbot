import os
import shutil
import requests
import zipfile

source = ['config.py',
          'localfuncs.py',
          'markups.py']
dest = 'C://assistbot'

try:
    os.remove('config.py')
    shutil.rmtree(dest)
except: pass
os.system('py cfggen.py')
os.system('pip install --upgrade pip')
os.system("pip install -r requirements.txt")
if not os.path.isdir('C:\\assistbot'):
    os.mkdir('C:\\assistbot')



for i in source:
    shutil.copy(f'{os.getcwd()}\{i}', dest)

link = 'https://www.nirsoft.net/utils/nircmd-x64.zip'
r = requests.get(link)

with open('nircmd.zip','wb') as f:
    f.write(r.content)

with zipfile.ZipFile('nircmd.zip', mode='r') as archive:
    archive.extract('nircmd.exe')


shutil.copy(f'{os.getcwd()}//nircmd.exe', dest)

os.remove('nircmd.zip')
os.remove('nircmd.exe')
os.remove('config.py')