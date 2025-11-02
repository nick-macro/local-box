from .base_classes.brew import BrewDependency

class DevContainer(BrewDependency):
    def __init__(self) -> None:
        self.name = "devcontainer"
        self.cask = False
        self.tap = None
