from .base_classes.brew import BrewDependency

class GitHub(BrewDependency):
    def __init__(self) -> None:
        self.name = "gh"
        self.cask = False
        self.tap = None
