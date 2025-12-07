/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
eval "$(/opt/homebrew/bin/brew shellenv)"

brew install git uv

mkdir -p $HOME/repos
mkdir -p $HOME/.local/bin

cd $HOME/repos
git clone git@github.com:nick-macro/local-box.git
uv tool install --editable .

echo "Setup complete! You can now use the `local-box` command to learn more."
