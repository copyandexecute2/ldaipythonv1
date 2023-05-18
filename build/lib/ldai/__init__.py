import importlib
import sys
import serial
import time

try:
    importlib.import_module('serial')
except ModuleNotFoundError:
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyserial'])

try:
    importlib.import_module('sys')
except ModuleNotFoundError:
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'sys'])

def px(value, **kwargs):
    color = kwargs.get('color', 'black')
    # Hier kannst du den Code für die px-Funktion hinzufügen, z.B.:
    print(f'Value: {value}, Color: {color}')


class LEDStrip:
    def __init__(self, name):
        self.name = name

    def select(self):
        ldai.led.selected_strip = self.name


class LDAI:
    def __init__(self):
        self.led = LEDManager()

    def px(self, value, **kwargs):
        color = kwargs.get('color', 'black')
        # Hier kannst du den Code für die px-Funktion hinzufügen, z.B.:
        print(f'Value: {value}, Color: {color}')

    def run(self):
        # Hier kannst du den Code hinzufügen, um die Animation zu starten und mit dem Arduino zu kommunizieren
        pass


class LEDManager:
    def __init__(self):
        self.selected_strip = None

    def select(self, strip_name, led_name):
        if self.selected_strip is not None:
            # Hier kannst du die Logik implementieren, um die LED auszuwählen und zu verwenden
            print(f'Selected LED: {led_name} in Strip: {strip_name}')
        else:
            print('No LED strip selected. Please select a strip before using LEDs.')


ldai = LDAI()


def animation(s, color='black', transition=True):
    if transition:
        # Führe Animation mit Übergang durch
        for i in range(s):
            ldai.px(i, color=color)
            send_to_arduino(f'Value: {i}, Color: {color}')
            time.sleep(0.5)  # Kurze Pause zwischen den Animationsschritten
    else:
        # Führe Animation ohne Übergang durch
        ldai.px(s-1, color=color)
        send_to_arduino(f'Value: {s-1}, Color: {color}')


def send_to_arduino(message):
    # Öffne die Verbindung zur Arduino über die serielle Schnittstelle
    ser = serial.Serial('COM3', 9600)  # Passe den COM-Port entsprechend an

    # Sende die Nachricht an die Arduino
    ser.write(message.encode())

    # Schließe die Verbindung zur Arduino
    ser.close()
