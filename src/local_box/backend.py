import subprocess
from importlib.resources import files
from pathlib import Path


def link_from_project_data(source: str, target: str) -> None:
    source = files("local_box.data").joinpath(source)
    target = Path(target).expanduser()

    target.unlink(missing_ok=True)
    target.symlink_to(source)


def sync() -> None:
    """
    Backend entry point for the sync operation.
    """

    dirs = [
        Path("~/.config/homebrew").expanduser(),
    ]
    for dir in dirs:
        dir.mkdir(parents=True, exist_ok=True)

    links = [
        {"source": "brewfile", "target": "~/.config/homebrew/Brewfile"},
        {"source": "zprofile", "target": "~/.zprofile"},
        {"source": "zshenv", "target": "~/.zshenv"},
        {"source": "zshrc", "target": "~/.zshrc"},
        {"source": "gitconfig", "target": "~/.gitconfig"},
    ]
    for link in links:
        link_from_project_data(link["source"], link["target"])

    # Use zsh -lic to source new environment variables
    subprocess.run(["zsh", "-lic", "brew bundle install"], check=True)
    subprocess.run(["zsh", "-lic", "brew bundle cleanup"], check=True)


def clean() -> None:
    """
    Backend entry point for the clean operation.
    """
    subprocess.run("docker system prune --all -f", shell=True, check=True)
    subprocess.run("brew cleanup --prune=all -s", shell=True, check=True)
    subprocess.run("uv cache clean", shell=True, check=True)
