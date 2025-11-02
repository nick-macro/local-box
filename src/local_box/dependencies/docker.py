import subprocess
from .base_classes.brew import BrewDependency

class Docker(BrewDependency):
    def __init__(self) -> None:
        self.name = "docker"
        self.cask = True
        self.tap = None

    def clean(self) -> None:
        super().clean()
        subprocess.run(["docker", "system", "prune", "-a", "-f", "--volumes"], check=True)
