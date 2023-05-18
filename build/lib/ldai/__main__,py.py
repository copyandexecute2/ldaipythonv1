import importlib
import sys

try:
    importlib.import_module('serial')
except ModuleNotFoundError:
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyserial'])

from ldai import *

def px(value, **kwargs):
    color = kwargs.get('color', 'black')
    # Hier kannst du den Code für die px-Funktion hinzufügen, z.B.:
    print(f'Value: {value}, Color: {color}')
