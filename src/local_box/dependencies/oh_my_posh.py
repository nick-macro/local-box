from .base_classes.brew import BrewDependency

class OhMyPosh(BrewDependency):
    def __init__(self) -> None:
        self.name = "oh-my-posh"
        self.cask = False
        self.tap = None
