from signal import signal, SIGINT
from sys import exit
from cursor.app import run

def handler(signal_received, frame):
    print(' CTRL-C detectado. Saliendo...')
    exit(0)

if __name__ == "__main__":
    signal(SIGINT, handler)
    run()