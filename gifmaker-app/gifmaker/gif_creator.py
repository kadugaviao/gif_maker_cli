"""
GIF creation and encoding.
"""

from pathlib import Path
from typing import List

import imageio.v3 as iio

from .constants import DEFAULT_DURATION, DEFAULT_LOOP


def create_gif(
    images: List,
    output_filename: str,
    duration: int = DEFAULT_DURATION,
    loop: int = DEFAULT_LOOP
) -> None:
    """
    Create an animated GIF from images.

    Args:
        images: List of image arrays
        output_filename: Output file name
        duration: Frame duration in milliseconds
        loop: Number of loops (0 = infinite)

    Raises:
        ValueError: Invalid parameters or no images
        RuntimeError: Failed to create GIF
    """
    if not images:
        raise ValueError("No images to create GIF")
    
    if duration <= 0:
        raise ValueError(f"Duration must be positive, got: {duration}")
    
    if loop < 0:
        raise ValueError(f"Loop count must be non-negative, got: {loop}")
    
    output_path = Path(output_filename)
    if output_path.suffix.lower() != '.gif':
        output_path = output_path.with_suffix('.gif')
    
    try:
        iio.imwrite(output_path, images, duration=duration, loop=loop)
        print(f"\n✓ GIF created successfully: '{output_path}'")
        print(f"  Frames: {len(images)}")
        print(f"  Duration per frame: {duration}ms")
        print(f"  Loop: {'infinite' if loop == 0 else loop}")
    except Exception as e:
        raise RuntimeError(f"Failed to create GIF: {e}")
