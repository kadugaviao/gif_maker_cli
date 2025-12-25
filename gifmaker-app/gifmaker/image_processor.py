"""
Image loading utilities.
"""

from pathlib import Path
from typing import List

import imageio.v3 as iio
from PIL import Image


def load_images(file_paths: List[Path]) -> List:
    """
    Load images from disk into memory and normalize dimensions.

    Args:
        file_paths: List of image file paths

    Returns:
        List of loaded image arrays with normalized dimensions

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
    
    # Normalize image dimensions
    if images:
        images = _normalize_dimensions(images)
    
    return images


def _normalize_dimensions(images: List) -> List:
    """
    Resize all images to match the first image's dimensions.

    Args:
        images: List of image arrays

    Returns:
        List of resized image arrays
    """
    if not images:
        return images
    
    # Get dimensions of first image
    first_shape = images[0].shape[:2]  # (height, width)
    target_size = (first_shape[1], first_shape[0])  # PIL uses (width, height)
    
    normalized = []
    for img in images:
        # Convert numpy array to PIL Image
        pil_img = Image.fromarray(img)
        
        # Resize to target dimensions
        resized = pil_img.resize(target_size, Image.Resampling.LANCZOS)
        
        # Convert back to numpy array
        normalized.append(__import__('numpy').array(resized))
    
    return normalized
