import subprocess

class HomeBrew:
    def __init__(self):
        return None

    @property
    def installed(self) -> bool:
        result = subprocess.run(
            ["which", "brew"],
            capture_output=True,
            text=True,
        )
        return result.returncode == 0

    def update(self):
        if self.installed:
            subprocess.run(["brew", "update"], check=True)
        else:
            subprocess.run(["/bin/bash", "-c", '"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'], check=True)

    def clean(self):
        if self.installed:
            subprocess.run(["brew", "cleanup", "--prune=all"], check=True)

    def uninstall(self):
        if self.installed:
            subprocess.run(["/bin/bash", "-c", '"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"'], check=True)
