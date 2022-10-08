"""Melon and Squash classes."""

import robots


class Melon:
    """Melon."""

    def __init__(self, melon_type):
        """Initialize melon.

        melon_type: type of melon being built.
        """

        self.melon_type = melon_type
        self.weight = 0.0
        self.color = None
        self.stickers = []

    def prep(self):
        """Prepare the melon."""

        robots.cleanerbot.clean(self)
        robots.stickerbot.apply_logo(self)

    def __str__(self):
        """Print out information about melon."""

        if self.weight <= 0:
            return self.melon_type
        else:
            return f"{self.color} {self.weight:.2f} lbs {self.melon_type}"


class Squash(Melon):
    """Winter squash."""

    # def __init__(self, melon_type):
    #     """Initialize the attributes of a Squash instance."""

    #     super().__init__("Winter Squash")

    def prep(self):
        
        """Prepare the squash"""
        super().prep()  # do not pass in self; that's already being done in the parent's prep method
        robots.painterbot.paint(self)

