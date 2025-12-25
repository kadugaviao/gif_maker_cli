"""
Image loading utilities.
"""

from pathlib import Path
from typing import List

import imageio.v3 as iio


def load_images(file_paths: List[Path]) -> List:
    """
    Load images from disk into memory.

    Args:
        file_paths: List of image file paths

    Returns:
        List of loaded image arrays

    Raises:
        RuntimeError: Failed to load an image
    """
    images = []
    
    for i, file_path in enumerate(file_paths, 1):
        try:
            image = iio.imread(file_path)
            images.append(image)
            print(f"Loaded {i}/{len(file_paths)}: {file_path.name}")
        except Exception as e:
            raise RuntimeError(f"Failed to load image '{file_path}': {e}")
    
    return images
