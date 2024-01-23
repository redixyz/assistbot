import requests
import zipfile
import os
dest = 'C://assistbot'

link = 'https://www.nirsoft.net/utils/nircmd-x64.zip'
r = requests.get(link)

with open('nircmd.zip', 'wb') as f:
    f.write(r.content)

with zipfile.ZipFile('nircmd.zip', mode='r') as archive:
    archive.extract('nircmd.exe', path=dest)
os.remove('nircmd.zip')