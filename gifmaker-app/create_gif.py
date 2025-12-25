#!/usr/bin/env python3
"""
GIF Maker - Entry point script.

This is a thin wrapper around the gifmaker package CLI.
For backward compatibility, this file preserves the original script interface.

You can also run the package directly:
    python3 -m gifmaker.cli
"""

from gifmaker.cli import main

if __name__ == "__main__":
    main()
