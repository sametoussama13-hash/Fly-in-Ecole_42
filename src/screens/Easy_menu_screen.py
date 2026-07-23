"""Display menu."""
from .screens import Screens
import pygame


class EasyMenu(Screens):
    """Class display menu."""

    def __init__(self) -> None:
        """Init display menu."""
        self.list_easy_menu = ["linear_path", "simple_fork", "basic_capacity", "Exit"]
        self.next_screen = None
        self.index = 0

    def handle_event(self, event: pygame.event) -> pygame.Surface:
        """Handle event."""
        if event == pygame.K_KP_ENTER:
            if self.index == 0:
                return 
            elif self.index == (len(self.list_easy_menu) - 1):
                return Screens.list_screens[-2]
        elif event == pygame.K_ESCAPE:
            return False
        elif event == pygame.K_DOWN:
            if self.index < (len(self.list_easy_menu) - 1):
                self.index += 1
        elif event == pygame.K_UP:
            if self.index > 0:
                self.index -= 1


    def update(self, dt: float) -> None:
        """Update."""
        pass

    def draw(self, screen: pygame.Surface) -> None: