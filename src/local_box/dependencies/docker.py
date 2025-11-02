from .base_classes.brew import BrewDependency

class Docker(BrewDependency):
    def __init__(self) -> None:
        self.name = "docker"
        self.cask = True
        self.tap = None
