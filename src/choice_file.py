"""Choice type file."""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]


def choice_file() -> str:
    """Choice file."""
    choice: int = 0
    level: str = ""
    while choice != 5:
        path: str = "/maps/"
        try:
            choice = int(input("Choice maps: \n"
                               "    1- Easy\n"
                               "    2- Medium\n"
                               "    3- Hard\n"
                               "    4- Challenge\n"
                               "    5- Exit\n"))
            if choice == 1:
                level = "Easy"
                path += "easy/"
                choice = int(input(f"   choice type of {level}:\n"
                                   "        1- linear_path\n"
                                   "        2- simple_fork\n"
                                   "        3- basic_capacity\n"
                                   "        5- Exit\n"
                                   "        Other number for return\n"))
                if choice == 1:
                    path += "01_linear_path.txt"
                    break
                elif choice == 2:
                    path += "02_simple_fork.txt"
                    break
                elif choice == 3:
                    path += "03_basic_capacity.txt"
                    break

            elif choice == 2:
                level = "Medium"
                path += "medium/"
                choice = int(input(f"   choice {level}:\n"
                                   "        1- dead_end_trap\n"
                                   "        2- circular_loop\n"
                                   "        3- priority_puzzle\n"
                                   "        5- Exit\n"
                                   "        Other number for return\n"))
                if choice == 1:
                    path += "01_dead_end_trap.txt"
                    break
                elif choice == 2:
                    path += "02_circular_loop.txt"
                    break
                elif choice == 3:
                    path += "03_priority_puzzle.txt"
                    break
            elif choice == 3:
                level = "Hard"
                path += "hard/"
                choice = int(input(f"   choice {level}:\n"
                                   "        1- maze_nightmare\n"
                                   "        2- capacity_hell\n"
                                   "        3- ultimate_challenge\n"
                                   "        5- Exit\n"
                                   "        Other number for return\n"))
                if choice == 1:
                    path += "01_maze_nightmare.txt"
                    break
                elif choice == 2:
                    path += "02_capacity_hell.txt"
                    break
                elif choice == 3:
                    path += "03_ultimate_challenge.txt"
                    break

            elif choice == 4:
                level = "Challenge"
                path += "/challenge"
                choice = int(input(f"   choice {level}:\n"
                                   "        1- the_impossible_dream\n"
                                   "        5- Exit\n"
                                   "        Other number for return\n"))
                if choice == 1:
                    path += "01_the_impossible_dream.txt"
                    break
        except ValueError as e:
            print(e)
            print("Just the numeric input has accepted.")
    return str(BASE_DIR) + path
