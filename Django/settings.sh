log()

{
    echo -e "\033[0;33m$1\033[0m"
}

log "========= Start !!! ========="

# 시간 설정
log "========= Time Set ========="
sudo timedatectl set-timezone 'Asia/Seoul'

# Apt-get 업데이트
log "========= Apt-get Update ========="
sudo apt-get update
sudo apt-get upgrade -y

# pyenv 설치하며 필요한 패키지 설치
log "========= App Install ========="
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev

# pyenv 설치 시작
log "========= Pyenv Install ========="
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

# bash_profile과 pyenv 설정
log "========= .bash_profile Settomg AND restart ========="
cd ~ && touch .bash_profile
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bash_profile

# bash_profile 재시작
source ~/.bash_profile

# 특정 버전의 파이썬 설치 및 global 선언
log "========= Python 3.9.8 Install AND Python Global ========="
log "========= There may be delays. ========="
pyenv install 3.9.8
pyenv global 3.9.8

# nginx 설치
log "========= Nginx Install ========="
sudo apt-get install -y nginx

# 가상환경 설치
log "========= Env Create ========="
python3 -m venv ~/env
cd ~/env

# pip upgrade
log "========= Pip Upgrade ========="
~/env/bin/python3 -m pip install --upgrade pip

# bash_profile 재시작
log ""========= .bash_profile Restart ========="
cd ~
source ~/.bash_profile

log ""========= End !!! ========="
