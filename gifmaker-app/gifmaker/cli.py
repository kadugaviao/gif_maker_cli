"""
Command-line interface and main entry point.
"""

import argparse
import sys

from .constants import DEFAULT_DURATION, DEFAULT_LOOP
from .validators import get_images_from_folder, validate_image_files
from .image_processor import load_images
from .gif_creator import create_gif


def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments.

    Returns:
        Parsed arguments
    """
    parser = argparse.ArgumentParser(
        description='Create animated GIFs from multiple images',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Create GIF from specific files
  %(prog)s img1.jpg img2.jpg img3.jpg --output animation.gif
  
  # Create GIF from all PNG files in a folder
  %(prog)s --folder images/ --pattern "*.png" --output slideshow.gif
  
  # Customize animation settings
  %(prog)s img1.jpg img2.jpg --output fast.gif --duration 100 --loop 5
        """
    )
    
    input_group = parser.add_mutually_exclusive_group(required=False)
    input_group.add_argument(
        'images',
        nargs='*',
        default=[],
        help='Image files to include in the GIF'
    )
    input_group.add_argument(
        '--folder',
        '-f',
        help='Folder containing images'
    )
    
    parser.add_argument(
        '--pattern',
        '-p',
        default='*',
        help='File pattern when using --folder (default: *)'
    )
    
    parser.add_argument(
        '--output',
        '-o',
        required=True,
        help='Output GIF filename'
    )
    
    parser.add_argument(
        '--duration',
        '-d',
        type=int,
        default=DEFAULT_DURATION,
        help=f'Duration per frame in milliseconds (default: {DEFAULT_DURATION})'
    )
    
    parser.add_argument(
        '--loop',
        '-l',
        type=int,
        default=DEFAULT_LOOP,
        help=f'Number of loops, 0 for infinite (default: {DEFAULT_LOOP})'
    )
    
    args = parser.parse_args()
    
    if not args.folder and not args.images:
        parser.error('Either provide image files or use --folder option')
    
    return args


def main() -> None:
    """
    Main entry point - orchestrates the entire workflow.
    """
    try:
        args = parse_arguments()
        
        if args.folder:
            print(f"Loading images from folder: {args.folder}")
            file_paths = get_images_from_folder(args.folder, args.pattern)
        else:
            print(f"Loading {len(args.images)} image(s)")
            file_paths = validate_image_files(args.images)
        
        images = load_images(file_paths)
        
        create_gif(
            images,
            args.output,
            duration=args.duration,
            loop=args.loop
        )
        
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user")
        sys.exit(130)
    except (FileNotFoundError, ValueError, RuntimeError) as e:
        print(f"\nError: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {e}", file=sys.stderr)
        sys.exit(1)
