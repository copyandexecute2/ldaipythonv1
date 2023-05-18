import serial
import time

def send_to_arduino(message):
    # Öffne die Verbindung zur Arduino über die serielle Schnittstelle
    ser = serial.Serial('COM3', 9600)  # Passe den COM-Port entsprechend an

    # Sende die Nachricht an die Arduino
    ser.write(message.encode())

    # Schließe die Verbindung zur Arduino
    ser.close()

def main():
    # Überprüfe, ob ein LED-Streifen angeschlossen ist
    try:
        with serial.Serial('COM3', 9600, timeout=1) as ser:
            ser.write(b'CHECK\n')
            time.sleep(1)  # Warte auf eine Antwort vom Arduino
            response = ser.readline().decode().strip()
            if response == 'LED_CONNECTED':
                # LED-Streifen ist angeschlossen
                print('LED-Streifen ist angeschlossen. Führe Durchlauf mit RGB-Beleuchtung aus.')
                send_to_arduino('RUN_RGB_ANIMATION')
            else:
                print('Kein LED-Streifen angeschlossen.')
    except serial.SerialException:
        print('Fehler beim Verbinden mit der seriellen Schnittstelle.')

if __name__ == '__main__':
    main()
