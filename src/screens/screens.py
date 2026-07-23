from abc import ABC, abstractmethod
import pygame


class Screens(ABC):
    """Class Screens."""

    list_screens: list["Screens"] = []

    @classmethod
    def add_screen(cls, screen: "Screens") -> None:
        """Add screen."""
        cls.list_screens.append(screen)

    @abstractmethod
    def update(self, dt: float) -> None:
        """Update."""
        pass

    @abstractmethod
    def handle_event(self, event: pygame.event) -> pygame.Surface:
        """Handle event."""
        pass

    @abstractmethod
    def draw(self, screen: pygame.Surface) -> None:
        """Draw."""
        pass
