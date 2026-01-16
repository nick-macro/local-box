
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

if [ "$(which gh)" = "/opt/homebrew/bin/gh" ]; then
    echo "✅ gh is installed via Homebrew. Skipping gh installation."
else
    echo "🔧 Homebrew installation of gh not detected. Installing gh via Homebrew."
    brew install gh
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
    echo "🔧 Installing local-box as a uv tool."
    uv tool install --editable $HOME/repos/local-box
fi


if ssh -T git@github.com 2>&1 | grep -q "successfully authenticated"; then
    echo "✅ GitHub ssh is configured. Skipping setup."
else
    echo "🔧 Setting up GitHub ssh."
    gh auth login -w -c -p ssh
fi

echo "⬇️ Recommended next step: run 'local-box sync' in the terminal."
