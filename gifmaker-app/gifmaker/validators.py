"""
File validation and discovery utilities.
"""

from pathlib import Path
from typing import List

from .constants import SUPPORTED_FORMATS


def get_images_from_folder(folder_path: str, pattern: str = '*') -> List[Path]:
    """
    Find all images in a folder matching the pattern.

    Args:
        folder_path: Path to the folder
        pattern: Filter pattern like '*.jpg' (default: all)

    Returns:
        List of image paths sorted alphabetically

    Raises:
        FileNotFoundError: Folder doesn't exist
        ValueError: No matching images found
    """
    folder = Path(folder_path)
    
    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder_path}")
    
    if not folder.is_dir():
        raise ValueError(f"Path is not a directory: {folder_path}")
    
    image_files = []
    for file_path in sorted(folder.glob(pattern)):
        if file_path.is_file() and file_path.suffix.lower() in SUPPORTED_FORMATS:
            image_files.append(file_path)
    
    if not image_files:
        raise ValueError(
            f"No images found in '{folder_path}' matching pattern '{pattern}'"
        )
    
    return image_files


def validate_image_files(filenames: List[str]) -> List[Path]:
    """
    Validate that all image files exist and have supported formats.

    Args:
        filenames: List of file paths

    Returns:
        List of validated paths

    Raises:
        FileNotFoundError: File doesn't exist
        ValueError: Empty list or unsupported format
    """
    if not filenames:
        raise ValueError("No image files provided")
    
    validated_paths = []
    for filename in filenames:
        file_path = Path(filename)
        
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {filename}")
        
        if file_path.suffix.lower() not in SUPPORTED_FORMATS:
            raise ValueError(
                f"Unsupported format: {filename} "
                f"(supported: {', '.join(sorted(SUPPORTED_FORMATS))})"
            )
        
        validated_paths.append(file_path)
    
    return validated_paths
