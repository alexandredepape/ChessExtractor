from os import mkdir
from os.path import join, exists

import image_slicer
import shortuuid

from src.config import ASSETS_DIRECTORY, OUTPUT_DIRECTORY
from src.pieces_extractor import get_raw_image_paths


def main():
    paths = get_raw_image_paths()
    for path in paths:
        tiles = image_slicer.slice(path, col=8, row=8, save=False)
        save_piece_images(tiles)
        # break


def save_piece_images(tiles):
    for piece_name, positions in COLOR_POSITIONS.items():
        extract_piece(piece_name, positions, tiles)


def extract_piece(piece_name, positions, tiles):
    piece_tiles = [tile for tile in tiles if tile.position in positions]
    output_path = join(ASSETS_DIRECTORY, OUTPUT_DIRECTORY, piece_name)
    if not exists(output_path):
        mkdir(output_path)
    uuid__random = shortuuid.ShortUUID().random(length=4)
    image_slicer.save_tiles(piece_tiles, directory=output_path, prefix=uuid__random, format='png')


if __name__ == '__main__':
    main()
