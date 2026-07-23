from pydantic import BaseModel, Field, model_validator
from typing import Any


class Connection(BaseModel):
    """Class Connection."""
    connection: tuple[str, str] = Field(...)
    max_link_capacity: int | None = Field(default=1)


class Hub(BaseModel):
    """Class hub."""
    name: str = Field(...)
    position: tuple[int, int] = Field(...)
    max_drones: int = Field(default=1, gt=0)
    color: str | None = Field(default=None)
    zone: str = Field(default="normal")
    list_connections: list[Connection] = Field(..., min_length=0)


class Maps(BaseModel):
    """Class maps."""

    nb_drones: int = Field(..., gt=0)
    hub_list: list[Hub] = Field(..., min_length=0)
    list_connections: list[Connection] = Field(..., min_length=0)

    @model_validator(mode="before")
    @classmethod
    def create_list_hub(cls, data: dict[Any]) -> list[Hub]:
        """Create list hub."""

        if not isinstance(data, dict):
            raise ("Error format of Data: Data most to be a dict")
        elif not data:
            raise ("Error data is empty")

        hubs: list[Hub] = []
        connections_list: list[Connection] = []
        hub_list: list[dict[Any]] = data["hub_list"]
        list_connections: list[dict[Any]] = data["list_connections"]

        if not hub_list:
            raise ("List hub is empty: we can't find hub")
        for dict_hub in hub_list:
            connections: list[Connection] = []
            for con in list_connections:
                if dict_hub["name"] in con["connection"]:
                    connection = Connection(**con)
                    connections.append(connection)
                    connections_list.append(connection)
            hub = Hub(**dict_hub, list_connections=connections)
            hubs.append(hub)
        data["hub_list"] = hubs
        data["list_connections"] = connections_list
        return data
