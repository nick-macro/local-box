from .base_classes.brew import BrewDependency

class VisualStudioCode(BrewDependency):
    def __init__(self) -> None:
        self.name = "visual-studio-code"
        self.cask = True
        self.tap = None
