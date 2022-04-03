import os, pathlib
from .levels import *


ASSET_DIR = f'{os.getcwd()}/res/textures'

TILE = 64

HEIGHT = len(level1) * TILE
WIDTH = 1200
FPS = 60
