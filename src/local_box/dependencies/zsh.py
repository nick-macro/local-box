from .base_classes.brew import BrewDependency
from pathlib import Path
from importlib.resources import files
import shutil

class Zsh(BrewDependency):
    def __init__(self):
        self.name = "zsh"
        self.cask = False
        self.tap = None

        self.zshrc_source = files("local_box.data").joinpath("zshrc")
        self.zshenv_source = files("local_box.data").joinpath("zshenv")
        self.zprofile_source = files("local_box.data").joinpath("zprofile")

        self.zshrc_target = Path.home() / ".zshrc"
        self.zshenv_target = Path.home() / ".zshenv"
        self.zprofile_target = Path.home() / ".zprofile"

    def add_zshrc(self) -> None:
        shutil.copy(self.zshrc_source, self.zshrc_target)

    def add_zshenv(self) -> None:
        shutil.copy(self.zshenv_source, self.zshenv_target)

    def add_zprofile(self) -> None:
        shutil.copy(self.zprofile_source, self.zprofile_target)

    def remove_zshrc(self) -> None:
        shutil.unlink(self.zshrc_target)

    def remove_zshenv(self) -> None:
        shutil.unlink(self.zshenv_target)

    def remove_zprofile(self) -> None:
        shutil.unlink(self.zprofile_target)

    def update(self):
        super().update()

        self.add_zshrc()
        self.add_zshenv()
        self.add_zprofile()


    def uninstall(self):
        super().uninstall()

        self.remove_zshrc()
        self.remove_zshrc()
        self.remove_zprofile()
