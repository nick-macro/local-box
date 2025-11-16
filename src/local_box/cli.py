import typer
from . import backend

app = typer.Typer(help="A simple CLI for managing local dependencies.")

@app.command()
def update() -> None:
    """
    Update managed dependencies.
    """
    typer.echo("Running update...")
    try:
        backend.update()
        typer.echo("Update completed.")
    except Exception as e:
        typer.echo(f"Update failed: {e}")
        raise typer.Exit(code=1)


@app.command()
def clean() -> None:
    """
    Clean up local caches.
    """
    typer.echo("Running clean...")
    try:
        backend.clean()
        typer.echo("Clean completed.")
    except Exception as e:
        typer.echo(f"Clean failed: {e}")
        raise typer.Exit(code=1)
