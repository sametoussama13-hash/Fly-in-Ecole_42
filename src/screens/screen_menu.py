"""Display menu."""
from .screens import Screens
from .Easy_menu_screen import EasyMenu
import pygame


class DisplayMenu(Screens):
    """Class display menu."""

    def __init__(self) -> None:
        """Init display menu."""
        self.list_menu = ["Choice maps:", "Easy", "Medium", "Hard",
                          "Challenge", "Exit"]
        self.next_screen = None
        self.index = 0

    def handle_event(self, event: pygame.event) -> pygame.Surface:
        """Handle event."""
        if event == pygame.K_KP_ENTER:
            if self.index == 0:
                self.next_screen = EasyMenu()
            elif self.index == (len(self.list_menu) - 1):
                return False
        elif event == pygame.K_ESCAPE:
            return False
        elif event == pygame.K_DOWN:
            if self.index < (len(self.list_menu) - 1):
                self.index += 1
        elif event == pygame.K_UP:
            if self.index > 0:
                self.index -= 1


    def update(self, dt: float) -> None:
        """Update."""
        pass

    def draw(self, screen: pygame.Surface) -> None:
        