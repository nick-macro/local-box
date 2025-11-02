import subprocess

class BrewDependency:
    @property
    def installed(self) -> bool:
        result = subprocess.run(["brew", "list", self.name], capture_output=True)
        return result.returncode == 0

    @property
    def tapped(self) -> bool:
        if self.tap is None:
            return True
        return self.tap in subprocess.run(["brew", "tap"], check=True, capture_output=True, text=True).stdout.splitlines()

    @property
    def cask_flag(self) -> str:
        return "--cask" if self.cask else ""

    def update(self) -> None:
        if not self.tapped:
            subprocess.run(["brew", "tap", self.tap], check=True)

        cmd = ["brew"]

        if self.installed:
            cmd += ["upgrade"]
        else:
            cmd += ["install"]

        if self.cask_flag:
            cmd += [self.cask_flag]

        cmd += [self.name]
        r = subprocess.run(cmd, check=True, text=True, capture_output=True)

        if len(r.stdout) > 0:
            print(r.stdout)
        if r.stderr:
            print(r.stderr)

    def clean(self) -> None:
        return None

    def uninstall(self) -> None:
        cmd = ["brew", "uninstall"]

        if self.cask_flag:
            cmd += [self.cask_flag]

        cmd += [self.name, "--zap", "--force"]
        subprocess.run(cmd, check=True)
