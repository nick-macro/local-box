/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
eval "$(/opt/homebrew/bin/brew shellenv)"

brew install git gh uv

# login to GitHub using the website (-w), copy the device code to the clipboard (-c), and use SSH for authentication (-p ssh)
gh auth login -w -c -p ssh

mkdir -p $HOME/repos
mkdir -p $HOME/.local/bin

cd $HOME/repos
git clone git@github.com:nick-macro/local-box.git
uv tool install --editable .

echo "Setup complete! You can now use the `local-box` command to learn more."
