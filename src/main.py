"""Main."""
from .parsing.read_text_file import parsing_file


def run(file: str) -> int:
    """Run programme."""
    maps = parsing_file(file)
    if not maps:
        print("Error parsing")
        return 0
    
    
