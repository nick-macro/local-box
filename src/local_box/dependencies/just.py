from .base_classes.brew import BrewDependency

class Just(BrewDependency):
    def __init__(self) -> None:
        self.name = "just"
        self.cask = False
        self.tap = None
