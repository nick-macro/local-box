from .base_classes.brew import BrewDependency

class ITerm(BrewDependency):
    def __init__(self) -> None:
        self.name = "iterm2"
        self.cask = True
        self.tap = None
