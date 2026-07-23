"""Display simulation."""
from .screens import DisplayMenu, Screens
import pygame


class Display:
    """Class display."""

    def __init__(self, screen_size: tuple[int, int] = (800, 800)) -> None:
        """Init Display"""
        self.screen_size = screen_size

    def play_simulation(self) -> int:
        """Play simulation"""
        try:
            pygame.init()
            clock = pygame.time.Clock()
            screen = pygame.display.set_mode(self.screen_size)
            current_screen: Screens = DisplayMenu()

            runing: bool = True

            while runing:
                for event in pygame.event.get():
                    if event == pygame.QUIT:
                        runing = False
                    elif event == pygame.KEYDOWN:
                        runing = current_screen.handle_event(event)
                        if current_screen.next_screen:
                            current_screen = current_screen.next_screen
                            current_screen.next_screen = None
                            if current_screen not in Screens.list_screens:
                                Screens.add_screen(current_screen)
                dt = clock(40) / 1000
                screen.fill((0, 0, 0))
                current_screen.update(dt)
                current_screen.draw()
                pygame.display.update()
            pygame.quit()

        except Exception as e:
            print(e)
