import cv2
import matplotlib.pyplot as plt
import mss
import pyautogui
import numpy as np
import struct
import pickle
import socket

WIDTH, HEIGHT = tuple(pyautogui.size())
class Screenshot:
    screen = None

    @classmethod
    def refresh(cls):
        try:
            with mss.mss() as sct:
                monitor = {'top': 0, 'left': 0, 'width': WIDTH, 'height': HEIGHT}
                im = np.asarray(sct.grab(monitor))
                cls.screen = cv2.cvtColor(im, cv2.COLOR_BGRA2BGR)
        except mss.exception.ScreenShotError as e:
            print('Error: Failed to capture screenshot')
            print('message:', e)
        return cls.screen

def send_payload(conn, l):
    data_str = pickle.dumps(l)
    conn.sendall(struct.pack('>I', len(data_str)) + data_str)

def receive_exact(conn, length):
    buffer = b''
    while len(buffer) < length:
        data = conn.recv(length - len(buffer))
        if not data:
            raise Exception("Connection lost")
        buffer += data
    return buffer

def receive_payload(conn):
    length = receive_exact(conn, 4)
    body_size = struct.unpack(">I", length)[0]
    body = receive_exact(conn, body_size)
    return pickle.loads(body)

class Bot:
    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            #s.connect(('95.216.11.230', 9999))
            s.connect(('localhost', 9999))
            while True:
                try:
                    print('Receive payload')
                    cmd = receive_payload(s)
                    print('Data received from client:')
                    print(cmd)
                    if cmd == 'screenshot':
                        screen = Screenshot.refresh()
                        send_payload(s, screen)
                    elif cmd == 'mouseDown':
                        print(f'Mouse down')
                        pyautogui.mouseDown()
                    elif cmd == 'mouseUp':
                        print(f'Mouse up')
                        pyautogui.mouseUp()
                    elif cmd == 'click':
                        print(f'click')
                        pyautogui.click()
                    elif isinstance(cmd, list):
                        if cmd[0] == 'moveTo':
                            print(f'Move coord {cmd[1]} {cmd[2]} {cmd[3]} {cmd[4]}')
                            pyautogui.moveTo(cmd[1], cmd[2], *cmd[3], **cmd[4])
                    else:
                        exit()
                except Exception as e:
                    print('Exception', e)
                    print('Break')
                    break

s = Bot()
s.run()

