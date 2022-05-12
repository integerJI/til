log()
{
    echo -e "\033[1;36m$1\033[0m"
}

log "Time Set"
sudo timedatectl set-timezone 'Asia/Seoul'

log "apt-get Update"
sudo apt-get update
sudo apt-get upgrade -y

log "Settings"
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev

log "Pyenv Install"
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

log ".bash_profile Settomg AND restart"
cd ~ && touch .bash_profile
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
source ~/.bash_profile

log "Python 3.9.8 Install AND Python Global"
pyenv install 3.9.8
pyenv global 3.9.8
