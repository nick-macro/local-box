set shell := ["zsh", "-cu"]

@_:
    just list

lint PATH=".":
    uv run ruff check --fix {{PATH}}

format PATH=".":
    uv run ruff format {{PATH}}
