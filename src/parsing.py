"""Parsing file."""
from .choice_file import choice_file
from pydantic import BaseModel, Field
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parents[0]

class Hub(BaseModel):
    """Class hub."""

class Maps(BaseModel):
    """Class maps."""
    nb_drones: int = Field(..., gt=0)
    list_hub: list[Hub] = Field(..., min_length=0)


def parsing_file(file: str) -> Maps:
    """Parsing file."""
    file_path: Path = BASE_DIR / file

    dict_file: dict[Any] = {"hub_list": []}

    if not file or not file_path.exists():
        file = choice_file()
        file_path = str(BASE_DIR) + file
    try:
        with open(file_path, 'r') as f:
            for all_line in f:
                all_line = all_line.strip()
                if all_line.startswith("#") or not all_line:
                    continue
                # elif all_line.startswith("nb_drones"):
                key, value = all_line.split(":")
                if key == "nb_drones":
                    value = value.strip()
                    dict_file[key] = int(value)
                elif "hub" in key:
                    dict_hub: dict = {}
                    hub, x, y, optionals = value.strip().split()

                    optionals = optionals.strip("[]").split()

                    for optional in optionals:
                        print(optional)
                        name, option = optional.split("=")
                        dict_hub[name] = option
                    position = (int(x), int(y))
                    dict_hub["name"] = hub
                    dict_hub["position"] = position
    
                    dict_file["hub_list"].append(dict_hub)
                
                elif key == "connection":
                    dict_dist: dict = {}
                    dict_file["dist_list"] = []
                    connection = value.strip().split()
                    if len(connection) > 2:
                        distination, capacity = connection
                        dict_dist["distination"] = distination
                        dict_dist["capacity"] = capacity
                    else:
                        dict_dist["distination"] = connection[0]

                    
                    dict_file["dist_list"].append(dict_dist)

                    
                    



            print(f"Dict: {dict_file}")
            # print(f"key : {key}, value : {value}")
            # print("all_line:", all_line)

    except Exception as e:
        print(e)