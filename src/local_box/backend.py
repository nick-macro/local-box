from .dependencies.dependencies import dependencies

def update() -> None:
    """
    Backend entry point for the update operation.
    """
    for dep in dependencies:
        dep.update()


def clean() -> None:
    """
    Backend entry point for the clean operation.
    """
    for dep in dependencies:
        dep.clean()


def uninstall() -> None:
    """
    Backend entry point for the uninstall operation.
    """
    for dep in dependencies:
        dep.uninstall()
