from .base_classes.brew import BrewDependency

class LocalStack(BrewDependency):
    def __init__(self) -> None:
        self.name = "localstack/tap/localstack-cli"
        self.cask = False
        self.tap = None
