echo "Installing homebrew..."
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
eval "$(/opt/homebrew/bin/brew shellenv)"

echo "Installing git and uv..."
brew install git uv

echo "Making repos directory..."
mkdir -p $HOME/repos
mkdir -p $HOME/.local/bin

echo "Installing local-box..."
cd $HOME/repos
git clone git@github.com:nick-macro/local-box.git
uv tool install --editable ./local-box

echo "Installing dependencies using local-box..."
uvx local-box sync
