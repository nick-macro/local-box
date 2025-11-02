from .base_classes.brew import BrewDependency

class NerdFont(BrewDependency):
    def __init__(self) -> None:
        self.name = "font-fira-code-nerd-font"
        self.cask = True
        self.tap = None
