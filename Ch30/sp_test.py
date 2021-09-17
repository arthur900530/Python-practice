import subprocess

path = r'C:\Users\user\AppData\Local\Programs\Python\Python39\python.exe'
pyPro = subprocess.Popen([path, 'sp.py'])
print(pyPro)