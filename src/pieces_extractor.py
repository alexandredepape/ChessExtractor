from os import listdir, mkdir
from os.path import isfile, join, exists

import image_slicer
import shortuuid

from src.config import ASSETS_DIRECTORY, RAW_DIRECTORY, OUTPUT_DIRECTORY, PIECE_POSITIONS


def save_piece_images(tiles):
    for piece_name, positions in PIECE_POSITIONS.items():
        extract_piece(piece_name, positions, tiles)


def extract_piece(piece_name, positions, tiles):
    piece_tiles = [tile for tile in tiles if tile.position in positions]
    output_path = join(ASSETS_DIRECTORY, OUTPUT_DIRECTORY, piece_name)
    if not exists(output_path):
        mkdir(output_path)
    uuid__random = shortuuid.ShortUUID().random(length=22)
    image_slicer.save_tiles(piece_tiles, directory=output_path, prefix=uuid__random, format='png')


def main():
    paths = get_raw_image_paths()
    for path in paths:
        print(path)
        tiles = image_slicer.slice(path, col=8, row=8, save=False)
        save_piece_images(tiles)
        # break


def get_raw_image_paths():
    raw_path = join(ASSETS_DIRECTORY, RAW_DIRECTORY)
    files = listdir(raw_path)
    paths = [join(raw_path, f) for f in files]
    return paths


if __name__ == '__main__':
    main()
