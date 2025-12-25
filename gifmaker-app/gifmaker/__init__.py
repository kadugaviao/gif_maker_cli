"""
GIF Maker - Create animated GIFs from your images!
"""

from .constants import DEFAULT_DURATION, DEFAULT_LOOP, SUPPORTED_FORMATS
from .validators import validate_image_files, get_images_from_folder
from .image_processor import load_images
from .gif_creator import create_gif

__version__ = "2.0.0"

__all__ = [
    'DEFAULT_DURATION',
    'DEFAULT_LOOP',
    'SUPPORTED_FORMATS',
    'validate_image_files',
    'get_images_from_folder',
    'load_images',
    'create_gif',
]
