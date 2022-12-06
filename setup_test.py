import os

def clr():
    os.system('powershell "cls"')

def activate():
    os.system('powershell ".venv\\Scripts\\activate.bat"')

#update pip if required
os.system('powershell "python.exe -m pip install --upgrade pip"')
os.system('powershell "py -m pip install requests"')
clr

#create venv if required
if not os.path.exists('.\\.venv'):
    print('Virtual Environment does not exist, Creating now...')
    os.system('powershell "py -m venv .venv"')
    print('Environment Created!')

clr
#attempt to activate venv
print('Activating Virtual Environment')
os.system('powershell ".venv\\scripts\\activate.ps1"')


clr
#attempt to install required modules
if os.path.exists('.\\requirements.txt'):
    print("Requirements file found attempting to install...")
    os.system('powershell "py -m pip install -r requirements.txt"')
else:
    print('No requirements file was found!')

print()
print('    v------ should now read (.venv), if it does not! paste : " .venv\\Scripts\\activate " into the console')


