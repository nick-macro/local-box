
if command -v brew &> /dev/null; then
    echo "✅ Homebrew detected. Skipping Homebrew installation."
else
    echo "🔧 Homebrew not detected. Installing Homebrew."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    eval "$(/opt/homebrew/bin/brew shellenv)"
fi

if [ "$(which uv)" = "/opt/homebrew/bin/uv" ]; then
    echo "✅ uv is installed via Homebrew. Skipping uv installation."
else
    echo "🔧 Homebrew installation of uv not detected. Installing uv via Homebrew."
    brew install uv
fi

REPO_PATH="$HOME/repos/local-box"
REPO_URL="git@github.com:nick-macro/local-box.git"

if [ -d "$REPO_PATH" ] && git -C "$REPO_PATH" rev-parse --git-dir &> /dev/null; then
    echo "✅ Repository detected. Skipping clone."
else
    echo "🔧 Cloning repository."
    git clone "$REPO_URL" "$REPO_PATH"
fi

if uv tool list | grep -q "^local-box "; then
    echo "✅ local-box is installed. Skipping installation."
else
    echo "🔧 local-box is not installed as a uv tool"
    uv tool install --editable $HOME/repos/local-box
fi

echo "🔧 Installing dependencies using local-box..."
uvx local-box sync
