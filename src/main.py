"""Main."""
from .parsing import parsing_file
from pathlib import Path


def run(file: str) -> int:
    """Run programme."""
    maps = parsing_file(file) 
