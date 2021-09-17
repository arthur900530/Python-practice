import subprocess

calcPro = subprocess.Popen('calc.exe')
notePro = subprocess.Popen('notepad.exe')
writePro = subprocess.Popen('write.exe')

print(notePro.wait())