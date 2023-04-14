from bot_server.utils import *
from bot_server.screenshot import Screenshot
from bot_server.client import Kingdom, Land
from bot_server.mouse import Mouse
import socket
import struct

TEST = True
ACCOUNT = 1
CONFIG = {'google_login': True, 'bot_options': {'gather':False, 'monsters': True, 'gather_crystal': True, 'use_spell': True, 'gather_min_level': 1, 'monster_max_level': 1}}
class Bot:
    def __init__(self):
        #self.kingdom = Kingdom(ACCOUNT, CONFIG)
        self.land = Land(ACCOUNT, CONFIG)


if __name__ == '__main__':
    print('Starting bot')

    def search_diamonds():
        for direction in b.land._random_walk(150):
            t = time.time()
            mine_coords = b.land._get_mines_on_screen()
            if time.time() - t > 3:
                print('Taking more than 3s to scan mines')
            if any(el[0] == 'crystal' for el in mine_coords):
                print('Found crystal mine')
                break
            print(mine_coords)
            go_direction = eval(f'Mouse.go_{direction}')
            go_direction()
            go_direction()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(('', 9999))
            s.listen()
            conn, addr = s.accept()
            print(f'Connected to {conn} {addr}')
            Screenshot.conn = conn
            Mouse.conn = conn
        except ConnectionResetError:
            pass

        b = Bot()
        search_diamonds()


