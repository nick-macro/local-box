import subprocess
from importlib.resources import files
import os

def update() -> None:
    """
    Backend entry point for the update operation.
    """

    dirs = [
        "$HOME/.config/homebrew",
    ]
    for dir in dirs:
        os.makedirs(os.path.expandvars(dir), exist_ok=True)

    links = [
        {"source": "brewfile", "target": "$HOME/.config/homebrew/Brewfile"},
        {"source": "zprofile", "target": "$HOME/.zprofile"},
        {"source": "zshenv", "target": "$HOME/.zshenv"},
        {"source": "zshrc", "target": "$HOME/.zshrc"},
        {"source": "vscode_keybindings", "target": "$HOME/Library/Application Support/Code/User/keybindings.json"},
        {"source": "vscode_settings", "target": "$HOME/Library/Application Support/Code/User/settings.json"},
    ]

    for link in links:
        source = files("local_box.data").joinpath(link["source"])
        target = os.path.expandvars(link["target"])

        subprocess.run(
            ["ln", "-sf", str(source), str(target)],
            check=True,
        )

    # Use zsh -lic to source new environment variables
    subprocess.run(["zsh", "-lic", "brew bundle install"], check=True)


def clean() -> None:
    """
    Backend entry point for the clean operation.
    """
    subprocess.run("docker system prune --all -f", shell=True, check=True)
    subprocess.run("brew cleanup --prune=all -s", shell=True, check=True)
    subprocess.run("uv cache clean", shell=True, check=True)
