"""
Application package settings.
"""
from setuptools import setup, find_packages

setup(
    name="hello_world_gui",
    version="0.1.0",
    description="Hello World GUI application with Tkinter",
    author="Python Developer",
    packages=find_packages(),
    install_requires=[
        # No external dependencies
    ],
    entry_points={
        'console_scripts': [
            'hello-world-gui=main:main',
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)