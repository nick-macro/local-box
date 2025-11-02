from .base_classes.brew import BrewDependency

class UV(BrewDependency):
    def __init__(self) -> None:
        self.name = "uv"
        self.cask = False
        self.tap = None
