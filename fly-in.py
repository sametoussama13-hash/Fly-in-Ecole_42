import sys
# from pathlib import Path
from src.main import run

# BASE_DIR = Path(__file__).resolve().parents[0]


def fly_in() -> None:
    """Entry fly_in."""
    path: str = ""
    if len(sys.argv) != 2:
        print("File argv[1] not find"
              "choice file existing.")
    else:
        path: str = sys.argv[1]

    sys.exit(run(path))


if __name__ == "__main__":
    fly_in()
