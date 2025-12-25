from setuptools import setup, find_packages

setup(
    name="gifmaker",
    version="1.0.0",
    description="CLI tool to create animated GIFs from images",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/gif",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "imageio>=2.31.0",
        "pillow>=10.0.0",
    ],
    entry_points={
        "console_scripts": [
            "gifmaker=gifmaker.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
