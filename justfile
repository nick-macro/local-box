set shell := ["zsh", "-cu"]

@_:
    just --list

# lint python files
lint PATH=".":
    uv run ruff check --fix {{PATH}}

# format python files
format PATH=".":
    uv run ruff format {{PATH}}

# type check python files
type PATH=".":
    uv run ruff format {{PATH}}

# run all checks
lgtm:
    just lint
    just format
    just type