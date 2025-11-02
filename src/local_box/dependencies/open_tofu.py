from .base_classes.brew import BrewDependency

class OpenTofu(BrewDependency):
    def __init__(self) -> None:
        self.name = "opentofu"
        self.cask = False
        self.tap = None
