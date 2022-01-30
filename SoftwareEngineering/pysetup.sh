#!/bin/bash
# Script now deprecated, was used in initial stages of project to launch app on remote server


echo "Script to install python and related packages for E2 instance."


echo "Installing Python 3.6 (stable)"

mkdir -p ~/miniconda3
#wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
wget https://repo.anaconda.com/miniconda/Miniconda3-4.3.11-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh


echo "Installing python packages"
conda install pandas
conda install sqlalchemy


echo "Installing MySQLdb, this is not supported in Ubuntu see SO link https://stackoverflow.com/a/23978968"
pip install mysqlclient
sudo apt-get install python3-dev libmysqlclient-dev



