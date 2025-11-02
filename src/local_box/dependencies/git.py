from .base_classes.brew import BrewDependency

class Git(BrewDependency):
    def __init__(self) -> None:
        self.name = "git"
        self.cask = False
        self.tap = None
