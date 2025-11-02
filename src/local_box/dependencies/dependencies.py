from .zsh import Zsh
from .homebrew import HomeBrew
from .visual_studio_code import VisualStudioCode
from .iterm import ITerm
from .docker import Docker
from .devcontainer import DevContainer
from .localstack import LocalStack
from .nerdfont import NerdFont
from .oh_my_posh import OhMyPosh
from .just import Just
from .open_tofu import OpenTofu
from .uv import UV
from .git import Git
from .git_hub import GitHub

dependencies = [
    Zsh(),
    HomeBrew(),
    VisualStudioCode(),
    ITerm(),
    Docker(),
    DevContainer(),
    LocalStack(),
    NerdFont(),
    OhMyPosh(),
    Just(),
    OpenTofu(),
    UV(),
    Git(),
    GitHub(),
]
