# Initial Setup
1. Install homebrew using `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
1. Add `brew` to your path with `eval "$(/opt/homebrew/bin/brew shellenv)"`
1. Install the GitHub CLI using `brew install gh`
1. Setup GitHub SSH with `gh auth login -c -p ssh -w`
1. Create a directory for all repos with `mkdir $HOME/repos && cd $HOME/repos`
1. Clone local-box (you are here!) with `git clone git@github.com:nick-macro/local-box.git`
1. Run the initial setup script with `./setup.sh`

# Maintenance
Consult `local-box --help` for commands.
