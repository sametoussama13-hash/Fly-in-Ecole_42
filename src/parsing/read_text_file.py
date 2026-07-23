"""Parsing file."""
from ..choice_file import choice_file
from .parsing_file import Maps
from pathlib import Path
from typing import Any
import re

BASE_DIR = Path(__file__).resolve().parents[1]


def parsing_file(file: str) -> Maps | None:
    """Parsing file."""
    file_path: Path = BASE_DIR / file

    data: dict[Any] = {"hub_list": []}

    if not file or not file_path.exists():
        file_path = choice_file()

    try:
        with open(file_path, 'r') as f:
            for all_line in f:
                all_line = all_line.strip()
                if all_line.startswith("#") or not all_line:
                    continue
                key, value = all_line.split(":")
                if key == "nb_drones":
                    value = value.strip()
                    data[key] = int(value)
                elif "hub" in key:
                    dict_hub: dict = {}
                    v = re.findall(r"\[.*?\]|\S+", value.strip())
                    hub, x, y, optionals = v
                    optionals = str(optionals).strip("[]").split()
                    for optional in optionals:
                        name, option = str(optional).split("=")
                        if option.isdigit():
                            option = int(option)
                        dict_hub[name] = option
                    dict_hub["name"] = hub
                    dict_hub["position"] = (int(x), int(y))
                    if "hub_list" not in data:
                        data["hub_list"] = []
                    data["hub_list"].append(dict_hub)
                elif key == "connection":
                    dict_dist: dict[Any] = {}
                    if "list_connections" not in data:
                        data["list_connections"] = []
                    connection = value.strip().split()
                    if len(connection) > 1:
                        distination, capacity = connection
                        a, b = distination.strip().split("-")
                        dict_dist["connection"] = (a, b)
                        name, max_capacity = capacity.strip("[]").split("=")
                        dict_dist[name] = int(max_capacity)
                    else:
                        a, b = connection[0].strip().split("-")
                        dict_dist["connection"] = (a, b)
                    data["list_connections"].append(dict_dist)

            return Maps(**data)

    except Exception as e:
        print(e)
        return
